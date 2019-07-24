from django.db import models

class Opinion(models.Model):
    FAVOR = 'A FAVOR'
    CONTRA = 'ENCONTRA'
    opciones = [
        (FAVOR, 'A FAVOR'),
        (CONTRA, 'ENCONTRA'),
    ]
    id = models.AutoField(primary_key=True)
    escritor = models.CharField(max_length=20, null=True)
    datetime = models.DateTimeField(auto_now=True)
    pre1 = models.TextField(max_length=296, blank=False, null=False)
    pre2 = models.TextField(max_length=296, blank=True, null=True)
    pre3 = models.CharField(choices=opciones, max_length=15, blank=False, null=False)

    class Meta:
        verbose_name = 'Opinion'
        verbose_name_plural = 'Opiniones'
        ordering = ["pre3"]  # Ordenar a la prox por nombre de usuario

    def __str__(self):
        return self.pre3  # Debe tener el nombre del usuario
