from django.shortcuts import render, redirect
from .models import Personal
# Create your views here.
    
def detalle(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "usuarios/detalle.html")

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

    return render(request, "usuarios/perfil.html")


