from datetime import datetime
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from usuarios.forms import AdminFormaCreacionUsuario, AdminFormaActualizar
from usuarios.models import Licencias, Personal, Puntajes, GruposGuardia, Licencias, Sanciones
from servicios.models import Servicios

# Register your models here.
class ServiciosToques(admin.TabularInline):
    model = Servicios.personal.through
    field = ['show_fecha', 'show_tipo']
    readonly_fields = ['show_fecha', 'show_tipo']
    extra=0
    verbose_name_plural = 'Servicios con toque'
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Servicios'
    def show_fecha(self, instance):
        return instance.servicios.t_toque
    show_fecha.short_description = 'Fecha'
    def show_tipo(self, instance):
        return instance.servicios.tipo
    show_tipo.short_description = 'Siniestro' 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(servicios__tipo_convocatoria = 't')
class EneroInlines(admin.TabularInline):
    model = Servicios.personal.through
    field = ['show_fecha', 'show_tipo']
    readonly_fields = ['show_fecha', 'show_tipo']
    extra=0
    verbose_name_plural = 'Servicios enero'
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Servicios'
    def show_fecha(self, instance):
        return instance.servicios.t_toque
    show_fecha.short_description = 'Fecha'
    def show_tipo(self, instance):
        if instance.servicios.tipo_convocatoria == 't':
            return 'TOQUE'
        else:
            return 'RADIOLLAMADA'
    show_tipo.short_description = 'Tipo' 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(servicios__t_toque__month = 1)
class FebreroInlines(admin.TabularInline):
    model = Servicios.personal.through
    field = ['show_fecha', 'show_tipo']
    readonly_fields = ['show_fecha', 'show_tipo']
    extra=0
    verbose_name_plural = 'Servicios febrero'
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Servicios'
    def show_fecha(self, instance):
        return instance.servicios.t_toque
    show_fecha.short_description = 'Fecha'
    def show_tipo(self, instance):
        if instance.servicios.tipo_convocatoria == 't':
            return 'TOQUE'
        else:
            return 'RADIOLLAMADA'
    show_tipo.short_description = 'Tipo' 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(servicios__t_toque__month = 2)
class MarzoInlines(admin.TabularInline):
    model = Servicios.personal.through
    field = ['show_fecha', 'show_tipo']
    readonly_fields = ['show_fecha', 'show_tipo']
    extra=0
    verbose_name_plural = 'Servicios marzo'
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Servicios'
    def show_fecha(self, instance):
        return instance.servicios.t_toque
    show_fecha.short_description = 'Fecha'
    def show_tipo(self, instance):
        if instance.servicios.tipo_convocatoria == 't':
            return 'TOQUE'
        else:
            return 'RADIOLLAMADA'
    show_tipo.short_description = 'Tipo' 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(servicios__t_toque__month = 3)
class AbrilInlines(admin.TabularInline):
    model = Servicios.personal.through
    field = ['show_fecha', 'show_tipo']
    readonly_fields = ['show_fecha', 'show_tipo']
    extra=0
    verbose_name_plural = 'Servicios abril'
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Servicios'
    def show_fecha(self, instance):
        return instance.servicios.t_toque
    show_fecha.short_description = 'Fecha'
    def show_tipo(self, instance):
        if instance.servicios.tipo_convocatoria == 't':
            return 'TOQUE'
        else:
            return 'RADIOLLAMADA'
    show_tipo.short_description = 'Tipo' 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(servicios__t_toque__month = 4)
class MayoInlines(admin.TabularInline):
    model = Servicios.personal.through
    field = ['show_fecha', 'show_tipo']
    readonly_fields = ['show_fecha', 'show_tipo']
    extra=0
    verbose_name_plural = 'Servicios mayo'
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Servicios'
    def show_fecha(self, instance):
        return instance.servicios.t_toque
    show_fecha.short_description = 'Fecha'
    def show_tipo(self, instance):
        if instance.servicios.tipo_convocatoria == 't':
            return 'TOQUE'
        else:
            return 'RADIOLLAMADA'
    show_tipo.short_description = 'Tipo' 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(servicios__t_toque__month = 5)
class JunioInlines(admin.TabularInline):
    model = Servicios.personal.through
    field = ['show_fecha', 'show_tipo']
    readonly_fields = ['show_fecha', 'show_tipo']
    extra=0
    verbose_name_plural = 'Servicios junio'
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Servicios'
    def show_fecha(self, instance):
        return instance.servicios.t_toque
    show_fecha.short_description = 'Fecha'
    def show_tipo(self, instance):
        if instance.servicios.tipo_convocatoria == 't':
            return 'TOQUE'
        else:
            return 'RADIOLLAMADA'
    show_tipo.short_description = 'Tipo' 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(servicios__t_toque__month = 6)
class JulioInlines(admin.TabularInline):
    model = Servicios.personal.through
    field = ['show_fecha', 'show_tipo']
    readonly_fields = ['show_fecha', 'show_tipo']
    extra=0
    verbose_name_plural = 'Servicios julio'
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Servicios'
    def show_fecha(self, instance):
        return instance.servicios.t_toque
    show_fecha.short_description = 'Fecha'
    def show_tipo(self, instance):
        if instance.servicios.tipo_convocatoria == 't':
            return 'TOQUE'
        else:
            return 'RADIOLLAMADA'
    show_tipo.short_description = 'Tipo' 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(servicios__t_toque__month = 7)
class AgostoInlines(admin.TabularInline):
    model = Servicios.personal.through
    field = ['show_fecha', 'show_tipo']
    readonly_fields = ['show_fecha', 'show_tipo']
    extra=0
    verbose_name_plural = 'Servicios agosto'
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Servicios'
    def show_fecha(self, instance):
        return instance.servicios.t_toque
    show_fecha.short_description = 'Fecha'
    def show_tipo(self, instance):
        if instance.servicios.tipo_convocatoria == 't':
            return 'TOQUE'
        else:
            return 'RADIOLLAMADA'
    show_tipo.short_description = 'Tipo' 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(servicios__t_toque__month = 8)
class SeptiembreInlines(admin.TabularInline):
    model = Servicios.personal.through
    field = ['show_fecha', 'show_tipo']
    readonly_fields = ['show_fecha', 'show_tipo']
    extra=0
    verbose_name_plural = 'Servicios septiembre'
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Servicios'
    def show_fecha(self, instance):
        return instance.servicios.t_toque
    show_fecha.short_description = 'Fecha'
    def show_tipo(self, instance):
        if instance.servicios.tipo_convocatoria == 't':
            return 'TOQUE'
        else:
            return 'RADIOLLAMADA'
    show_tipo.short_description = 'Tipo' 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(servicios__t_toque__month = 9)
class OctubreInlines(admin.TabularInline):
    model = Servicios.personal.through
    field = ['show_fecha', 'show_tipo']
    readonly_fields = ['show_fecha', 'show_tipo']
    extra=0
    verbose_name_plural = 'Servicios octubre'
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Servicios'
    def show_fecha(self, instance):
        return instance.servicios.t_toque
    show_fecha.short_description = 'Fecha'
    def show_tipo(self, instance):
        if instance.servicios.tipo_convocatoria == 't':
            return 'TOQUE'
        else:
            return 'RADIOLLAMADA'
    show_tipo.short_description = 'Tipo' 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(servicios__t_toque__month = 10)
class NoviembreInlines(admin.TabularInline):
    model = Servicios.personal.through
    field = ['show_fecha', 'show_tipo']
    readonly_fields = ['show_fecha', 'show_tipo']
    extra=0
    verbose_name_plural = 'Servicios noviembre'
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Servicios'
    def show_fecha(self, instance):
        return instance.servicios.t_toque
    show_fecha.short_description = 'Fecha'
    def show_tipo(self, instance):
        if instance.servicios.tipo_convocatoria == 't':
            return 'TOQUE'
        else:
            return 'RADIOLLAMADA'
    show_tipo.short_description = 'Tipo' 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(servicios__t_toque__month = 11)
class DiciembreInlines(admin.TabularInline):
    model = Servicios.personal.through
    field = ['show_fecha', 'show_tipo']
    readonly_fields = ['show_fecha', 'show_tipo']
    extra=0
    verbose_name_plural = 'Servicios diciembre'
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Servicios'
    def show_fecha(self, instance):
        return instance.servicios.t_toque
    show_fecha.short_description = 'Fecha'
    def show_tipo(self, instance):
        if instance.servicios.tipo_convocatoria == 't':
            return 'TOQUE'
        else:
            return 'RADIOLLAMADA'
    show_tipo.short_description = 'Tipo' 
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(servicios__t_toque__month = 12)

class InlinesLicencias(admin.TabularInline):
    model = Licencias
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Licencias'
    def show_fecha_inicio(self, instance):
        return instance.servicios.t_toque
    show_fecha_inicio.short_description = 'Fecha inicio'

class InlinesSanciones(admin.TabularInline):
    model = Sanciones
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    classes = ['collapse']
    can_delete = False
    def __str__(self):
        return 'Sanciones'
    field = ['titulo', 'dias', 'adjunto']
    readonly_fields = ['titulo', 'dias', 'adjunto']
    exclude = ['descripcion']
    extra=0
    verbose_name_plural = 'Sanciones'

class UserAdmin(BaseUserAdmin):
    class Media:
        css = {
            'all': ('usuarios/css/custom_admin.css', )     # Include extra css
        }
    inlines = [InlinesLicencias, InlinesSanciones, ServiciosToques, EneroInlines, FebreroInlines, MarzoInlines, AbrilInlines, MayoInlines, JunioInlines, JulioInlines,
    AgostoInlines, SeptiembreInlines, OctubreInlines, NoviembreInlines, DiciembreInlines]
    form = AdminFormaActualizar
    add_form: AdminFormaCreacionUsuario
    
    readonly_fields=('last_login', 'antiguedad', 'servicios_totales', 'servicios_con_toque_anual', 'servicios_con_toque_mensual',
    'asistencia_anual', 'asistencia_mensual', 'porcentaje_toques_anual', 'porcentaje_asistencias_anual', 'porcentaje_toques_mensual', 
    'porcentaje_asistencias_mensual', 'puntaje_toques_anual', 'puntaje_toques_mensual', 'puntaje_asistencias_anual', 'puntaje_asistencias_mensual',
    'grupo_guardia', 'puntaje_guardias_mensual', 'puntaje_guardias_anual', 'puntaje_oi_anual', 'puntaje_oi_mensual',
    'puntaje_total_anual', 'puntaje_total_mensual')
    list_display = ('matricula','get_full_name', 'jerarquia' , 'admin', 'seccion')
    list_filter = ('admin', 'seccion','jerarquia', 'cuerpo',)
    fieldsets = (
        (None, {'fields': ('matricula', 'password')}),
        ('Información personal', {'fields': (('nombre', 'apellido'),'sexo', ('correo', 'documento'), ('fecha_nacimiento', 'lugar_nacimiento'), 'foto_perfil')}),
        ('Información cuartel', {'fields': (('cuerpo', 'jerarquia'),'fecha_alta', ('seccion', 'grupo_guardia'), 'estudios')}),
        ('Permisos', {'fields': ('admin', 'staff', 'active')}),
        ('Otros', {'fields': ('last_login', 'antiguedad')}),
        ('Servicios', {'fields': ('servicios_totales', ('servicios_con_toque_anual', 'servicios_con_toque_mensual'),
        ('asistencia_anual', 'asistencia_mensual'),)}),
        ('Porcentajes', {'fields': (('porcentaje_toques_anual', 'porcentaje_toques_mensual'), ('porcentaje_asistencias_anual', 'porcentaje_asistencias_mensual'))}),
        ('Puntajes', {'fields': (('puntaje_total_anual', 'puntaje_total_mensual'), ('puntaje_toques_anual', 'puntaje_toques_mensual'), ('puntaje_asistencias_anual', 'puntaje_asistencias_mensual'),
        ('puntaje_guardias_anual', 'puntaje_guardias_mensual'), ('puntaje_oi_anual', 'puntaje_oi_mensual'),)}),
    )
    
    exclude = ('groups', 'is_active', 'last_name', 'is_staff', 'email', 'username', 'first_name', 'date_joined', 'is_superuser', 'user_permissions')

    add_fieldsets = (
        (None, {'fields': ('matricula', 'password1', 'password2', )}),
    )
    radio_fields = {'sexo':admin.HORIZONTAL}
    search_fields = ('matricula', 'apellido', 'nombre', 'jerarquia', 'seccion')
    ordering = ('jerarquia',)
    filter_horizontal = ()

class PuntajeAdmin(admin.ModelAdmin):
    readonly_fields=()
    list_display = ('persona', 'mes')
    list_filter = ('mes', 'persona', 'persona__seccion')
    fieldsets = (
        (None, {'fields': ('persona', 'mes',)}),
        ('Orden interno', {'fields': ('orden_interno', )}),
        ('Guardias', {'fields': ('guardias',)}),
    )

    search_fields = ('persona__matricula', 'persona__apellido', 'persona__nombre', 'persona__jerarquia', 'persona__seccion')
    ordering = ()
    filter_horizontal = ()

class GruposGuardiaAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'encargado_guardia')
    readonly_fields = ('encargado_guardia',)
    fieldsets = (
        (None, {'fields': ('grupo', 'encargado_guardia')}),
        ('Miembros', {'fields': ('miembros', )}),
    )
    filter_horizontal = ('miembros',)
    ordering = ('grupo',)

class LicenciasAdmin(admin.ModelAdmin):
    list_display = ('persona', 'inicio', 'finalizacion', 'tipo', 'activa')
    readonly_fields = ()
    fieldsets = (
        (None, {'fields': ('persona', 'tipo')}),
        ('Fechas', {'fields': ('inicio', 'finalizacion' )}),
    )
    filter_horizontal = ()
    ordering = ()

class CursosAdmin(admin.ModelAdmin):
    filter_horizontal = ('participantes', )

admin.site.register(Personal, UserAdmin)
admin.site.register(Puntajes, PuntajeAdmin)
admin.site.register(GruposGuardia, GruposGuardiaAdmin)
admin.site.register(Licencias, LicenciasAdmin)
admin.site.register(Sanciones)

