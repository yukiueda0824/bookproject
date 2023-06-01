from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm
)
from django.contrib.auth import get_user_model
from .models import Myprofile

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

class MyPasswordChangeForm(PasswordChangeForm):
    """パスワード変更フォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class MyprofileCreateForm(forms.ModelForm):
    class Meta:
        model = Myprofile
        fields = '__all__'
        widgets = {
            'joingtime': forms.SelectDateWidget(years=[x for x in range(2000, 2040)])
        }
