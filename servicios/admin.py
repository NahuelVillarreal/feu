from django.contrib import admin
from .models import  Asistencias, Servicios, Imagenes
# Register your models here.
class ImagenesInline(admin.TabularInline):
    model = Imagenes
    extra = 1

#class CondicionInline(admin.TabularInline):
#    model = Condicion
#    extra = 1
#    autocomplete_fields = ['persona',]

class ServicioAdmin(admin.ModelAdmin):
    inlines = [ImagenesInline,]
    list_display = ('n_servicio','t_toque', 'tipo')
    list_filter = ('tipo_convocatoria', 'tipo', 't_toque','personal')
    preserve_filters = True
    fieldsets = (
        ("General", {'fields': (('tipo', 'tipo_convocatoria'), 't_toque', ("f_salida", "h_salida"), ("f_llegada", "h_llegada"), "solicitante", ("dni_solicitante", "tel_solicitante"),)}),
        ('Ubicación', {'fields': ('zona', ('provincia','ciudad'), ('calle', 'numero'), 'entre_calles', ('ruta', 'km'))}),
        ('Propietario', {'fields': (('propietario', 'dni_propietario'),('tel_propietario', 'dom_propietario'), ('seguro', "n_poliza"))}),
        ('Servicio', {'fields': ('metodo_ataque', 'obs', 'vehiculos', 'personal')}),
    )

    add_fieldsets = (
        (None, {'fields': ('tipo', 'tipo_convocatoria', 't_toque', )}),
    )
    
    search_fields = ('personal__apellido', 'personal__nombre', 'personal__matricula')
    ordering = ('n_servicio',)
    filter_horizontal = ('vehiculos', 'personal')

class AsistenciasAdmin(admin.ModelAdmin):
    filter_horizontal = ('personal_asistencia',)

admin.site.register(Servicios, ServicioAdmin)
admin.site.register(Asistencias, AsistenciasAdmin)
