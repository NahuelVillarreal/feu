from django.conf import settings
from django.db import models
import os

# Create your models here.
def path_fotos(instance, filename):  #define ruta de archivo
    ruta = os.path.join(settings.MEDIA_ROOT, '{}/unidad{}/{}.JPG'.format("unidades", instance.unidad.numero, filename))
    return ruta

class Unidades(models.Model):
    PROPOSITO = [("V", "VIVIENDA"), ("F", "FORESTAL"), ("R", "RESCATE"), ("T", "TRANSPORTE"), ("O", "OTROS")]
    #caracteristicas
    numero = models.SmallIntegerField()
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20, blank=True)
    agno = models.SmallIntegerField(verbose_name='Año')
    proposito = models.CharField(max_length=1, choices=PROPOSITO)
    dominio = models.CharField(max_length=7)
    novedades = models.TextField(blank=True)
    activa = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Unidad"
        verbose_name_plural = "Unidades"
    
    def __str__(self):
        return 'Unidad N°{}'.format(self.numero)

class ImagenesVehiculos(models.Model):
    unidad = models.ForeignKey(Unidades, on_delete=models.CASCADE)
    imagenes = models.ImageField(upload_to=path_fotos)
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
