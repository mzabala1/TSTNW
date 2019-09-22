from apps.usuario.forms import RegistroForm
from django.conf import settings
from django.contrib import messages
from urllib import parse, request
from django.shortcuts import render, redirect

import json
import urllib


def Registro_Usuario(request):
    form = RegistroForm(request.POST)
    if form.is_valid():
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        print(response)
        print(result)
        ''' End reCAPTCHA validation '''
        if request.method == 'POST':
            form.save()
            messages.success(request, 'Nueva opinión añadida correctamente!')
        else:
            messages.error(request, 'reCAPTCHA invalido, intentalo nuevamente.')

        return redirect('login')

    return render(request, 'registration/registro.html', {'form': form})


def index(request):
    return render(request, 'base/index.html')
