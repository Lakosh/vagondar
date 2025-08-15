from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import models


class CustomLoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'login-inp',
        'placeholder': 'Имя пользователя',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'password-inp',
        'placeholder': 'Пароль',
    }))
