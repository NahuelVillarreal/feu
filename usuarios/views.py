from django.shortcuts import render, redirect, get_object_or_404
from servicios.models import Servicios
from .models import *
from .forms import FormularioDatos
from django.contrib import messages
# Create your views here.
    
def detalle(request):
    if not request.user.is_authenticated:
        return redirect('login')
    toques = Servicios.objects.filter(personal=request.user, tipo_convocatoria="t").order_by("t_toque")
    
    return render(request, "usuarios/detalle.html",{
        "toques":toques,
    })

def hacer_oi(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "usuarios/hacer-oi.html")

def inicio(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "usuarios/inicio.html")

def perfil(request):
    if not request.user.is_authenticated:
        return redirect('login')
    sexo = Personal.SEXO
    estado_civil = Personal.ESTADO_CIVIL
    tipos_sangre = Personal.TIPOS_DE_SANGRE
    cursos = Cursos.objects.filter(participantes=request.user).order_by("t_inicio_curso")
    licencias = Licencias.objects.filter(persona=request.user).order_by("inicio")
    sanciones = Sanciones.objects.filter(sancionado=request.user).order_by("fecha")
    return render(request, "usuarios/perfil.html", {
        "SEXO":sexo, 
        "ESTADO_CIVIL":estado_civil, 
        "TIPOS":tipos_sangre,
        "cursos":cursos,
        "licencias":licencias,
        "sanciones":sanciones,
        })

def editar_perfil(request):
    sexo = Personal.SEXO
    estado_civil = Personal.ESTADO_CIVIL
    tipos_sangre = Personal.TIPOS_DE_SANGRE
    if not request.user.is_authenticated:
        return redirect('login')
    elif request.method=="POST":
        form = FormularioDatos(request.POST, request.FILES, instance=request.user)
        files = request.FILES.getlist('estudios')
        if form.is_valid():
            form.save()
            if files:  # check if user has uploaded some files
                for file in files:
                    Estudios.objects.create(persona=request.user, 
                    estudio=file, 
                    tipo=filename,
                    fecha_subida=datetime.today().strftime('%Y-%m-%d'))
            messages.success(request, 'Datos guardados.')
            return redirect("perfil")
        else:
            messages.error(request, 'Información incorrecta.')
    
    form = FormularioDatos(instance=request.user)
    return render(request, "usuarios/editar-perfil.html", {
        "SEXO":sexo, 
        "ESTADO_CIVIL":estado_civil, 
        "TIPOS":tipos_sangre,
        "form":form
        })
