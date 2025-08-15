from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.http import FileResponse, Http404
from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
import os
from .forms import CustomLoginForm


@staff_member_required
def download_db(request):
    db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')
    if not os.path.exists(db_path):
        raise Http404("База данных не найдена")
    return FileResponse(open(db_path, 'rb'), as_attachment=True, filename='db.sqlite3')


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
