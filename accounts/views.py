from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.contrib.auth.views import  PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth import get_user_model
from django.conf import settings
from .consts import ITEM_PER_PAGE

from .forms import (
    SignupForm, MyPasswordChangeForm,MyprofileCreateForm
)
from .models import Myprofile
# Create your views here.

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('index')

class MyPageView(ListView):
    model = Myprofile
    template_name = 'accounts/mypage.html'

class PasswordChange(PasswordChangeView):
    form_class = MyPasswordChangeForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'registration/password_change.html'

class PasswordChangeDone(PasswordChangeDoneView):
    template_name = 'registration/password_change_finish.html'

class MyprofileCreate(CreateView):
    form_class = MyprofileCreateForm
    success_url = reverse_lazy('accounts:mypage')
    template_name = 'accounts/myprofile_create.html'

class ProfileListView(ListView):
    model = Myprofile
    paginate_by = ITEM_PER_PAGE
    template_name = 'accounts/profile_list.html'

class ProfileDetailView(DetailView):
    model = Myprofile
    template_name = 'accounts/profile_detail.html'

class ProfileUpdateView(UpdateView):
    model = Myprofile
    fields = '__all__'
    success_url = reverse_lazy('accounts:list_profile')
    template_name = 'accounts/profile_update.html'