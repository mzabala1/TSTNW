from django.urls import path
from .views import Registro_Usuario, index

app_name = "UsuarioApp"

urlpatterns = [
        path('registro/', Registro_Usuario, name="Registrarse"),
        path('', index, name="index"),
]
