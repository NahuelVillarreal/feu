from tabnanny import verbose
from django.db import models

# Create your models here.

class Unidades(models.Model):
    PROPOSITO = [("V", "VIVIENDA"), ("F", "FORESTAL"), ("R", "RESCATE"), ("T", "TRANSPORTE"), ("O", "OTROS")]
    #caracteristicas
    numero = models.SmallIntegerField()
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    agno = models.SmallIntegerField(verbose_name='Año')
    proposito = models.CharField(max_length=1, choices=PROPOSITO)
    dominio = models.CharField(max_length=7)

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"
