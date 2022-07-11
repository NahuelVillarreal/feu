from django.urls import path
from django.conf import settings
from usuarios import views
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import re_path

urlpatterns = [
    path('detalle', views.detalle, name="detalle"),
    path('hacer-oi', views.hacer_oi, name="hacer-oi"),
    path('inicio', views.inicio, name="inicio"),
    path('perfil', views.perfil, name="perfil"),

]

