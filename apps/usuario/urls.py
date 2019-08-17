from django.urls import path
from .views import RegistroUsuario, index

app_name = "UsuarioApp"

urlpatterns = [
        path('registro/', RegistroUsuario.as_view(), name="Registrarse"),
        path('', index, name="index"),
]
