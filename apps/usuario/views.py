from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroForm
from django.shortcuts import render


class RegistroUsuario(CreateView):

    model = User
    template_name = "registration/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')


def index(request):
    return render(request, 'base/index.html')

