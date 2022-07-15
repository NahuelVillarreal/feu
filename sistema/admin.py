from django.contrib import admin
from .models import ImagenesVehiculos, Unidades
# Register your models here.

class ImagenesUnidadesInline(admin.TabularInline):
    model = ImagenesVehiculos
    extra = 0
    classes = ['collapse']

class VehiculosAdmin(admin.ModelAdmin):
    inlines = [ImagenesUnidadesInline, ]
    list_display = ('__str__', 'marca', 'proposito', 'activa')

admin.site.register(Unidades, VehiculosAdmin)
