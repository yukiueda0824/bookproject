from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views 

from .views import SignupView,MyPageView, PasswordChange, PasswordChangeDone,MyprofileCreate, ProfileListView, ProfileDetailView, ProfileUpdateView


app_name = 'accounts'


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('mypage/', MyPageView.as_view(), name='mypage'),
    path('myprofile_create/', MyprofileCreate.as_view(), name='myprofile'),
    path('profile/', ProfileListView.as_view(), name='list_profile'),
    path('profile/<int:pk>/detail/', ProfileDetailView.as_view(), name='detail_profile'),
    path('profile/<int:pk>/update/', ProfileUpdateView.as_view(), name='update_profile'),
    path('password_change_form/', PasswordChange.as_view(), name='password_change_form'),    
    path('password_change_done/', PasswordChangeDone.as_view(), name='password_change_done'), 
]