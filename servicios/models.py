from tabnanny import verbose
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from sistema.models import Unidades
from usuarios.models import Personal
import datetime
import os

def path_fotos(instance, filename):  #define ruta de archivo
    ruta = os.path.join(settings.MEDIA_ROOT, '{}/{}/{}/{}.JPG'.format("servicios", instance.servicio.f_salida.year, instance.servicio.n_servicio, filename))
    return ruta
# Create your models here.
#Modelo servicios
class Servicios(models.Model):
    #CHOICES
    TOQUE = [("r", "Radiollamado"), ("t", "Toque de sirena")]
    ZONA = [("u", "Urbana"), ("r", "Ruta")]
    TIPO = [("V", "VIVIENDA"), ("F", "FORESTAL"), ("A", "ACCIDENTE"), ("R", "RESCATE"), ("C", "COLABORACION"), ("I", "INUNDACION"), ("D", "DESASTRE")]
    #generales
    t_toque = models.DateTimeField(default=datetime.datetime.now, verbose_name="Fecha y hora parte")
    tipo_convocatoria = models.CharField(max_length=1, choices=TOQUE, blank=True, verbose_name="Tipo convocatoria")
    f_salida = models.DateField(default=datetime.date.today,verbose_name="Fecha salida")
    h_salida = models.TimeField(null=True, blank=True, verbose_name="Hora salida")
    f_llegada = models.DateField(default=datetime.date.today, null=True, verbose_name="Fecha arribo")
    h_llegada = models.TimeField(null=True, blank=True, verbose_name="Hora arribo")
    n_servicio = models.AutoField(primary_key=True, verbose_name="Servicio N°")
    solicitante = models.CharField(max_length=50, blank=True, verbose_name="Nombre solicitante")
    dni_solicitante = models.IntegerField(null=True, blank=True, verbose_name="DNI")
    tel_solicitante = models.IntegerField(null=True, blank=True, verbose_name="Telefono")
    #ubicacion
    zona = models.CharField(max_length=1, choices=ZONA, blank=True)
    provincia = models.CharField(max_length=50, default="Buenos Aires", blank=True)
    ciudad = models.CharField(max_length=50, default="Punta Alta", blank=True)
    calle = models.CharField(max_length=50, blank=True)
    numero = models.SmallIntegerField(null=True, blank=True)
    entre_calles = models.CharField(max_length=80, blank=True)
    ruta = models.CharField(max_length=20, blank=True)
    km = models.SmallIntegerField(null=True, blank=True)
    
    #servicio
    metodo_ataque = models.CharField(max_length=50, blank=True)
    obs = models.TextField(blank=True, verbose_name="Observaciones")
    tipo = models.CharField(max_length=1, choices=TIPO, blank=True, null=True, verbose_name="Tipo servicio")
    vehiculos = models.ManyToManyField(Unidades, blank=True)
    personal = models.ManyToManyField(Personal, blank=True, related_name='personal')
    
    class Meta:
        verbose_name = ('Servicio')
        verbose_name_plural = ('Servicios')

    def __str__(self):
        return 'Servicio N° {}/{}'.format(str(self.n_servicio), str(self.t_toque.year))

class Asistencias(models.Model):
    MOTIVOS = [('A', 'ASISTENCIA'), ('C', 'CAPACITACIÓN'), ('D', 'CEREMONIAS'), ('O', 'OTROS')]
    n_asistencia = models.AutoField(primary_key=True, verbose_name="Asistencia N°")
    t_asistencia_inicio = models.DateTimeField(default=datetime.datetime.now, verbose_name='Fecha y hora de inicio')
    t_asistencia_fin = models.DateTimeField(null=True, blank=True, verbose_name='Fecha y hora finalización')
    motivo = models.CharField(max_length=1, choices=MOTIVOS, blank=True)
    observaciones = models.TextField(blank=True, verbose_name='Observaciones')
    personal_asistencia = models.ManyToManyField(Personal, blank=True, related_name='personal_asistencia')

    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

    def __str__(self):
        return 'Asistencia N°' + str(self.n_asistencia) + '/' + str(self.t_asistencia_inicio.year)

#modelos auxiliares
class Imagenes(models.Model):
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    imagenes = models.ImageField(upload_to=path_fotos)
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

class Involucrados(models.Model):
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    persona = models.CharField(max_length=50, blank=True)
    razon = models.CharField(max_length=50, blank=True)
    dni = models.IntegerField(null=True, blank=True, verbose_name="DNI")
    tel = models.IntegerField(null=True, blank=True, verbose_name="Telefono")
    dom = models.CharField(max_length=60, blank=True, verbose_name="Domicilio")
    extra = models.TextField(blank=True, verbose_name="Observaciones")
    class Meta:
        verbose_name = 'Persona involucrada'
        verbose_name_plural = 'Personas involucradas'

class VehiculosInvolucrados(models.Model):
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE)
    tipo_vehiculo = models.CharField(max_length=50, blank=True, verbose_name="Tipo de vehículo")
    marca = models.CharField(max_length=30, blank=True)
    modelo = models.CharField(max_length=30, blank=True)
    dominio = models.CharField(max_length=30, blank=True)
    agno = models.IntegerField(null=True, verbose_name="Año")
    extra1 = models.TextField(blank=True, verbose_name="Observaciones")
    class Meta:
        verbose_name = 'Vehiculo involucrado'
        verbose_name_plural = 'Vehiculos involucrados'