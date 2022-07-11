from django.shortcuts import render, redirect

# Create your views here.

def acerca_de(request):
    if not request.user.is_authenticated:
        return redirect('login')    

    return render(request, "sistema/acerca-de.html")
    
def documentacion(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, "sistema/documentacion.html")

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