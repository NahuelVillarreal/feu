from tabnanny import verbose
from django.db import models
from django.conf import settings
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
import os
from datetime import datetime

#<---------------------------------Modelo de usuarios------------------------------------->
# Create your models here.

def path_fotos(instance, filename):  #define ruta de archivo
    ruta = os.path.join(settings.MEDIA_ROOT, '{}/{}-{}.JPG'.format("fotos-perfil", instance.nombre, instance.apellido))
    if os.path.exists(ruta):
        os.remove(ruta)
    return '{}/{}-{}.JPG'.format("fotos-perfil", instance.nombre, instance.apellido)

def path_estudios(instance, filename):  #define ruta de archivo
    ext = filename.split('.')[-1]
    return '{}/{}_{}/{}_{}.{}'.format("estudios", instance.nombre, instance.apellido, datetime.today().strftime('%Y-%m-%d') , filename, ext)

class ManejadorUsuario(BaseUserManager):

    def create_user(self, matricula, password=None):
        usuario = self.model(matricula=matricula)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_staffuser(self, matricula, password):
        usuario = self.create_user(
            matricula,
            password=password,
        )
        usuario.staff = True
        usuario.save(using=self._db)
        return usuario
    
    def create_superuser(self, matricula, password):
        usuario = self.create_user(
            matricula,
            password=password,
        )
        usuario.staff = True
        usuario.admin = True
        usuario.save(using=self._db)
        return usuario


class Personal(AbstractBaseUser): #creo modelo de usuarios personalizado
    #reset
    #DATOS PERSONALES
    TIPOS_DE_SANGRE = [('O-', 'O NEGATIVO'), ('O+', 'O POSITIVO'), ('A-', 'A NEGATIVO'), ('A+', 'A POSITIVO'), ('B-', 'B NEGATIVO'), ('B+', 'B POSITIVO'), ('AB-', 'AB NEGATIVO'), ('AB+', 'AB POSITIVO')]
    SEXO = [('M', 'MASCULINO'),('F', 'FEMENINO'), ('O', 'OTRO')]
    ESTADO_CIVIL = [('S', 'SOLTERO'), ('C', 'CASADO'), ('D', 'DIVORCIADO'), ('V', 'VIUDO')]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(verbose_name='correo electrónico', max_length=100, unique=True, blank=True, null=True)
    documento = models.IntegerField(blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    lugar_nacimiento = models.CharField(max_length=50, blank=True)
    sexo = models.CharField(max_length=9, choices= SEXO, blank=True)
    grupo_sanguineo = models.CharField(max_length=20, choices=TIPOS_DE_SANGRE, blank=True)
    foto_perfil = models.ImageField(upload_to=path_fotos, blank=True, null=True)
    estudios = models.FileField(upload_to=path_estudios, blank=True, null=True)

    #DATOS CUARTELISTICOS
    JERARQUIAS = [('AS', 'ASPIRANTE'), ('BO', 'BOMBERO'), ('SS', 'SUBOF. SUBAYUDANTE'), ('SA', 'SUBOF. AYUDANTE'), ('SA1', 'SUBOF. AYUDANTE DE 1RA'), ('SAP', 'SUBOF. AYUDANTE PRINCIPAL'), 
    ('SAM', 'SUBOF. AYUDANTE MAYOR'), ('O3', 'OF. 3ERO'), ('O2', 'OF. 2DO'), ('O1', 'OF. 1ERO'), ('SC', 'SUBCOMANDANTE'), ('C', 'COMANDANTE'), ('CM', 'COMANDANTE MAYOR'), ('CG', 'COMANDANTE GENERAL') ]
    CUERPO = [('A', 'ACTIVO'), ('R', 'RESERVA'), ('I', 'INACTIVO'), ('O', 'OTRO')]
    SECCIONES = [('JE', 'JEFATURA'), ('EQ', 'EQUIPOS'), ('AU', 'AUTOMOTORES'), ('PE', 'PERSONAL'), ('OT', 'OTROS')]
    matricula = models.CharField(max_length=5, unique=True, primary_key=True)
    cuerpo = models.CharField(max_length=20, choices=CUERPO, blank=True)
    jerarquia = models.CharField(max_length=20, choices=JERARQUIAS, blank=True)
    seccion = models.CharField(max_length=20, choices=SECCIONES, blank=True)
    fecha_alta = models.DateField(blank=True, null=True)

    #parametros
    active = models.BooleanField(('Activo'), default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = ManejadorUsuario()

    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('Miembro')
        verbose_name_plural = ('Miembros')

    @property
    def is_staff(self):
        #usuario staff pero no superuser?
        return self.staff

    @property
    def is_admin(self):
        #usuario admin superuser?
        return self.admin

    @property
    def is_active(self):
        #usuario activo?
        return self.active

    def get_full_name(self):
        return self.apellido + ' '+ self.nombre
    get_full_name.short_description = 'Nombre'
    
    def get_short_name(self):
        return self.nombre

    def has_perm(self, perm, obj=None):
        "¿El usuario cuenta con un permiso en específico?"
        return True
    
    def has_module_perms(self, app_label):
        "¿El usuario cuenta con los permisos para ver una app en específico?"
        return True

    def antiguedad(self):
        import datetime
        today = datetime.date.today()
        someday = datetime.date(self.fecha_alta.year, self.fecha_alta.month, self.fecha_alta.day)
        diff = (today - someday).days
        agnos = str(int(diff/365))
        dias = str(diff%365)
        return agnos + ' años y ' + dias + ' dias'

    #servicios cantidades
    def servicios_totales(self):
        return self.personal.count()

    def servicios_con_toque_anual(self):
        return self.personal.filter(tipo_convocatoria = 't').count()
    
    def servicios_con_toque_mensual(self):
        return self.personal.filter(tipo_convocatoria = 't').filter(t_toque__month = datetime.now().month).count()

    def asistencia_anual(self):
        return self.personal_asistencia.count()
    
    def asistencia_mensual(self):
        return self.personal_asistencia.filter(t_asistencia_inicio__month = datetime.now().month).count()

    #porcentajes
    def porcentaje_toques_anual(self):
        from servicios.models import Servicios
        try:
            porc = 100*self.personal.filter(tipo_convocatoria = 't').count()/Servicios.objects.filter(tipo_convocatoria = 't').count()
        except ZeroDivisionError:
            porc = 100.0
        return str(round(porc,2)) + '%'

    def porcentaje_toques_mensual(self):
        from servicios.models import Servicios
        try:
            porc = 100*self.personal.filter(tipo_convocatoria = 't', t_toque__month = datetime.now().month).count()/Servicios.objects.filter(tipo_convocatoria = 't', t_toque__month = datetime.now().month).count()
        except ZeroDivisionError:
            porc = 100.0
        return str(round(porc,2)) + '%'

    def porcentaje_asistencia_anual(self):
        from servicios.models import Asistencias
        try:
            porc = 100*self.personal_asistencia.count()/Asistencias.objects.count()
        except ZeroDivisionError:
            porc = 100.0
        return str(round(porc,2)) + '%'

    def porcentaje_asistencia_mensual(self):
        from servicios.models import Asistencias
        try:
            porc = 100*self.personal_asistencia.filter(t_asistencia_inicio__month = datetime.now().month).count()/Asistencias.objects.filter(t_asistencia_inicio__month = datetime.now().month).count()
        except ZeroDivisionError:
            porc = 100.0
        return str(round(porc,2)) + '%'   

    #puntajes
    def puntaje_toques_anual(self):
        from servicios.models import Servicios
        suma = 0
        for mes in range(1, datetime.now().month+1):
            try:
                suma += 20*self.personal.filter(tipo_convocatoria = 't', t_toque__month = mes).count()/Servicios.objects.filter(tipo_convocatoria = 't', t_toque__month = mes).count()
            except ZeroDivisionError:
                suma +=20.0
        return str(round(suma, 2))

    def puntaje_toques_mensual(self):
        from servicios.models import Servicios
        try:
            suma = 20*self.personal.filter(tipo_convocatoria = 't', t_toque__month = datetime.now().month).count()/Servicios.objects.filter(tipo_convocatoria = 't').filter(t_toque__month = datetime.now().month).count()
        except ZeroDivisionError:
            suma = 20.0
        return str(round(suma, 2))

    def puntaje_asistencias_anual(self):
        from servicios.models import Asistencias
        suma = 0
        for mes in range(1, datetime.now().month+1):
            try:
                suma += 20*self.personal_asistencia.filter(t_asistencia_inicio__month = mes).count()/Asistencias.objects.filter(t_asistencia_inicio__month = mes).count()
            except ZeroDivisionError:
                suma +=20.0
        return str(round(suma, 2))

    def puntaje_asistencias_mensual(self):
        from servicios.models import Asistencias
        try:
            suma = 20*self.personal_asistencia.filter(t_asistencia_inicio__month = datetime.now().month).count()/Asistencias.objects.filter(t_asistencia_inicio__month = datetime.now().month).count()
        except ZeroDivisionError:
            suma = 20.0
        return str(round(suma, 2))

    def puntaje_guardias_anual(self):
        qs = Puntajes.objects.filter(persona_id=self.matricula).all()
        puntaje_total = 0
        for objeto in range(qs.count()):
            puntaje_total += qs[objeto].guardias
        return puntaje_total

    def puntaje_guardias_mensual(self):
        qs = Puntajes.objects.filter(persona_id=self.matricula, mes=datetime.now().month).all()
        puntaje_total = 0
        for objeto in range(qs.count()):
            puntaje_total += qs[objeto].guardias
        return puntaje_total

    def puntaje_oi_anual(self):
        qs = Puntajes.objects.filter(persona_id=self.matricula).all()
        puntaje_total = 0
        for objeto in range(qs.count()):
            puntaje_total += qs[objeto].orden_interno
        return puntaje_total

    def puntaje_oi_mensual(self):
        qs = Puntajes.objects.filter(persona_id=self.matricula, mes=datetime.now().month).all()
        puntaje_total = 0
        for objeto in range(qs.count()):
            puntaje_total += qs[objeto].orden_interno
        return puntaje_total

    def puntaje_total_anual(self):
        return (float(self.puntaje_asistencias_anual())+float(self.puntaje_guardias_anual())+float(self.puntaje_oi_anual())+float(self.puntaje_toques_anual()))

    def puntaje_total_mensual(self):
        return (float(self.puntaje_asistencias_mensual())+float(self.puntaje_guardias_mensual())+float(self.puntaje_oi_mensual())+float(self.puntaje_toques_mensual()))

    def grupo_guardia(self):
        return GruposGuardia.objects.filter(miembros=self.matricula)[0]

    def __str__(self):
        return self.apellido.upper() + ', ' + self.nombre

class Puntajes(models.Model):
    MES = [(1, 'ENERO'), (2, 'FEBRERO'), (3, 'MARZO'), (4, 'ABRIL'), (5, 'MAYO'), (6, 'JUNIO'), (7, 'JULIO'), 
    (8, 'AGOSTO'), (9, 'SEPTIEMBRE'), (10, 'OCTUBRE'), (11, 'NOVIEMBRE'), (12, 'DICIEMBRE'), ]
    persona = models.ForeignKey(Personal, null=True, on_delete=models.CASCADE, related_query_name='persona')
    mes = models.IntegerField(default=datetime.now().month, choices=MES)
    orden_interno = models.IntegerField(null=True, blank=True)
    guardias = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Puntaje'
        verbose_name_plural = 'Puntajes'

    def __str__(self):
        return self.persona.apellido

class Licencias(models.Model):
    TIPOS = [('A', 'Anual'), ('C', 'Casamiento'), ('E', 'Estudio'), ('I', 'Enfermedad'), ('F', 'Fallecimiento de Familiar'), 
    ('N', 'Nacimiento'), ('P', 'Embarazo')]
    persona = models.ForeignKey(Personal, null=True, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    finalizacion = models.DateTimeField()
    tipo = models.CharField(max_length=1, choices=TIPOS)
    
class GruposGuardia(models.Model):
    GRUPOS = [(1, 'GRUPO 1'), (2, 'GRUPO 2'), (3, 'GRUPO 4'), (4, 'GRUPO 4')]
    grupo = models.IntegerField(choices=GRUPOS, primary_key=True)
    miembros = models.ManyToManyField(Personal, blank=True, related_name='miembros')

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'

    def __str__(self):
        return str(self.grupo)