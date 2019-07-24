from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import  CreateView
from django.urls import reverse_lazy


class RegistroUsuario(CreateView):

    model = User
    template_name = "user/registro.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('/admin')