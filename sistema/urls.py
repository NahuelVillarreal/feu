from django.urls import path
from sistema import views


urlpatterns = [
    path('acerca-de', views.acerca_de, name="acerca-de"),
    path('personal/documentacion', views.documentacion, name="documentacion"),
    path('equipos/inventario', views.inventario, name="inventario"),
    path('automotores/parque-de-vehiculos', views.parque_de_vehiculos, name="parque-de-vehiculos"),
    path('personal/roperia', views.roperia, name="roperia"),
]

