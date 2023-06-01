from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Avg
from django.core.paginator import Paginator
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Book,Review
from .consts import ITEM_PER_PAGE
from django.utils import dateformat
from datetime import datetime

# Create your views here.
class ListBookView(LoginRequiredMixin, ListView):
    template_name = 'book/book_list.html'
    model = Book
    paginate_by = ITEM_PER_PAGE
    
class DetailBookView(LoginRequiredMixin, DetailView):
    template_name = 'book/book_detail.html'
    model = Book
    
class CreateBookView(LoginRequiredMixin, CreateView):
    template_name = 'book/book_create.html'
    model = Book
    fields = ('title', 'text', 'category', 'thumbnail')
    success_url = reverse_lazy('list-book')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)
    
class DeleteBookView(LoginRequiredMixin, DeleteView):
    template_name = 'book/book_confirm_delete.html'
    model = Book
    success_url = reverse_lazy('list-book')
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj
    
class UpdateBookView(LoginRequiredMixin, UpdateView):
    template_name = 'book/book_update.html'
    model = Book
    fields = ('title', 'text', 'category', 'thumbnail')
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        
        if obj.user != self.request.user:
            raise PermissionDenied
        
        return obj
    
    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk': self.object.id})
    
class CreateReviewView(LoginRequiredMixin, CreateView):
    model = Review
    fields = ('book', 'title', 'text', 'rate')
    template_name = 'book/review_form.html'
    d = datetime.now()
    Review.time =dateformat.format(d, 'Y-n-d')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book'] = Book.objects.get(pk=self.kwargs['book_id'])
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('detail-book', kwargs={'pk': self.object.book.id})



def index_view(request):
    object_list = Book.objects.order_by('-id')
    ranking_list = Book.objects.annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')
    laungage_list = Book.objects.filter(category='プログラミング言語').annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')
    game_list = Book.objects.filter(category='ゲーム開発').annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')
    system_list = Book.objects.filter(category='システム').annotate(avg_rating=Avg('review__rate')).order_by('-avg_rating')

    
    laungagepaginator = Paginator(laungage_list, ITEM_PER_PAGE)
    gamepaginator = Paginator(game_list, ITEM_PER_PAGE)
    systempaginator = Paginator(system_list, ITEM_PER_PAGE)
    page_number = request.GET.get('page',1)
    laungagepage_obj = laungagepaginator.page(page_number)
    gamepage_obj = gamepaginator.page(page_number)
    systempage_obj = systempaginator.page(page_number)

    
    return render(
        request,
        'book/index.html',
        {'object_list': object_list, 'ranking_list': ranking_list, 'laungage_list':laungage_list,
          'laungagepage_obj':laungagepage_obj, 'gamepage_obj':gamepage_obj, 'systempage_obj':systempage_obj},
    )


