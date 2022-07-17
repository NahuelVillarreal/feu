from django.contrib import admin
from .models import  Asistencias, Servicios, Imagenes, Involucrados, VehiculosInvolucrados
# Register your models here.
class ImagenesInline(admin.TabularInline):
    model = Imagenes
    extra = 0
    classes = ['collapse']

class InvolucradosInline(admin.StackedInline):
    model = Involucrados
    extra = 0
    classes = ['collapse']
    fieldsets = (
        (None, {'fields': (('persona','dni', 'dom', 'tel' ), ('razon', 'extra'))}),
    )

class VehiculosInvolucradosInline(admin.StackedInline):
    model = VehiculosInvolucrados
    extra = 0
    classes = ['collapse']
    fieldsets = (
        (None, {'fields': (('tipo_vehiculo','marca', 'modelo', 'agno', 'dominio'), 'extra1')}),
    )

class ServicioAdmin(admin.ModelAdmin):
    inlines = [InvolucradosInline, VehiculosInvolucradosInline, ImagenesInline]
    list_display = ('__str__','t_toque', 'tipo')
    list_filter = ('tipo_convocatoria', 'tipo', 't_toque','personal')
    preserve_filters = True
    fieldsets = (
        ("General", {'fields': (('tipo', 'tipo_convocatoria'), 't_toque', ("f_salida", "h_salida"), ("f_llegada", "h_llegada"), "solicitante", ("dni_solicitante", "tel_solicitante"),)}),
        ('Ubicación', {'fields': ('zona', ('provincia','ciudad'), ('calle', 'numero'), 'entre_calles', ('ruta', 'km'))}),
        ('Servicio', {'fields': ('metodo_ataque', 'obs', 'vehiculos', 'personal')}),
    )

    add_fieldsets = (
        (None, {'fields': ('tipo', 'tipo_convocatoria', 't_toque', )}),
    )
    
    search_fields = ('personal__apellido', 'personal__nombre', 'personal__matricula', 't_toque__month', 'tipo', 'tipo_convocatoria')
    ordering = ('n_servicio',)
    filter_horizontal = ('vehiculos', 'personal')

class AsistenciasAdmin(admin.ModelAdmin):
    filter_horizontal = ('personal_asistencia',)
    list_display = ('__str__', 't_asistencia_inicio', 'motivo')
    list_filter = ('motivo', 't_asistencia_inicio', 'personal_asistencia')
    search_fields = ('personal_asistencia__apellido', 'personal_asistencia__nombre', 'personal_asistencia__matricula', 'motivo')
    ordering = ('n_asistencia',)
admin.site.register(Servicios, ServicioAdmin)
admin.site.register(Asistencias, AsistenciasAdmin)
