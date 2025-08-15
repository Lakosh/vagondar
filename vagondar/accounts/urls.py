from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .forms import CustomLoginForm

urlpatterns = [
    path('login/', LoginView.as_view(template_name="accounts/login_page.html", authentication_form=CustomLoginForm), name="login"),
    path('logout/', LogoutView.as_view(next_page="login"), name='logout'),
    path('profile/', views.ProfileView.as_view(), name="profile")
]
