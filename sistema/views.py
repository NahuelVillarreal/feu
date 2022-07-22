from django.shortcuts import render, redirect
from .models import Documentacion

# Create your views here.

def acerca_de(request):
    if not request.user.is_authenticated:
        return redirect('login')    

    return render(request, "sistema/acerca-de.html")
    
def documentacion(request):
    if not request.user.is_authenticated:
        return redirect('login')
    documentos = Documentacion.objects.all().order_by('fecha_publicacion')
    oi = documentos.filter(tipo="O")
    cap = documentos.filter(tipo='C')
    mod = documentos.filter(tipo='M')
    otros = documentos.filter(tipo='D')
    return render(request, "sistema/documentacion.html", {
        'ordenes_internas':oi, 'capacitacion':cap, 'modulos':mod, 'otros':otros
    })

def inventario(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "sistema/inventario.html")

def parque_de_vehiculos(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "sistema/parque-de-vehiculos.html")

def roperia(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "sistema/roperia.html")