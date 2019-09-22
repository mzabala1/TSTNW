from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from snowpenguin.django.recaptcha2.widgets import ReCaptchaWidget
from snowpenguin.django.recaptcha2.fields import ReCaptchaField

# Formulario de Registro
class RegistroForm(UserCreationForm):
    captcha = ReCaptchaField(widget=ReCaptchaWidget(attrs={'classs': 'validate'}), label="")

    class Meta:
        model = User
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                  ]
        labels = {'username': 'Nombre de usuario',
                  'first_name': 'Nombre',
                  'last_name': 'Apellidos',
                  'email': 'Correo',
                  }
