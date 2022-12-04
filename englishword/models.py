from django.db import models


class RegistroPalabra(models.Model):
    tipo_palabra = models.CharField(max_length=50)
    palabra = models.CharField(max_length=50)
    significado = models.CharField(max_length=500)

    def __str__(self):
        texto = "type: {0}  word: {1}  traslate: {2}"
        return texto.format(self.tipo_palabra, self.palabra, self.significado)
# Create your models here.
