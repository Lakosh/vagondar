from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.models import User
from .forms import CustomLoginForm


class LoginView(DjangoLoginView):
    template_name = "accounts/login_page.html"


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/register_page.html"


class ProfileView(DetailView):
    model = User
    template_name = "accounts/profile.html"
    context_object_name = "profile_user"

    def get_object(self):
        return self.request.user
