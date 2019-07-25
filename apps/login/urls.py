from django.urls import path
from .views import RegistroUsuario

app_name = "TSTNW"

urlpatterns = [
        path('registrar', RegistroUsuario.as_view(), name="Registrarse"),
]
