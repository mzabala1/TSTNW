from django.db import models
from django.contrib.auth.models import User

class Opinion(models.Model):
    FAVOR = 'A FAVOR'
    CONTRA = 'ENCONTRA'
    opciones = [
        (FAVOR, 'A FAVOR'),
        (CONTRA, 'ENCONTRA'),
    ]
    escritor = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    fecha = models.DateTimeField(auto_now=True)
    pre1 = models.TextField(max_length=296, blank=False, null=False)
    pre2 = models.TextField(max_length=296, blank=True, null=True)
    pre3 = models.CharField(choices=opciones, max_length=15, blank=False, null=False)

    class Meta:
        verbose_name = 'Opinion'
        verbose_name_plural = 'Opiniones'
        ordering = ["fecha"]  # Ordenar a la prox por nombre de usuario

    def __str__(self):
        return self.pre3  # Debe tener el nombre del usuario
