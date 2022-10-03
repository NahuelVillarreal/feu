from django.urls import path
from cuarteleros import views


urlpatterns = [
    path('', views.logear2, name="logincuarteleros"),
    path('standby', views.standby, name="standby"),
    path('agnadir-servicio', views.agnadir_servicio, name="agnadir-servicio"),
    path('agnadir-asistencia', views.agnadir_asistencia, name="agnadir-asistencia"),
    path('servicios', views.servicios, name="servicios"),
    path('asistencias', views.asistencias, name="asistencias"),
    path('personal', views.personal, name="personal"),
]

