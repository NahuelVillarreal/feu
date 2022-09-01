from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.logear, name="login"),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
    path('change_pass', views.change_pass, name='change_pass'),

]
