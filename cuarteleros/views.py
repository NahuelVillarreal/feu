from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from usuarios.models import Personal
from django.contrib.auth.decorators import login_required

# Create your views here.

def logear2(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name__in=['Cuarteleros']):
            return redirect('standby')
        else:
            return redirect('inicio')
    elif request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            usuario = authenticate(matricula = nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('standby')
        else:
            messages.error(request, 'Información incorrecta.')
            return redirect('logincuarteleros')

    form = AuthenticationForm()
    return render(request, 'cuarteleros/logincuarteleros.html', {'form':form})

def standby(request):
    if request.user.groups.filter(name__in=['Cuarteleros']):
        return render(request, "cuarteleros/standby.html")
    else:
        logout(request)
        messages.error(request, 'No eres cuartelero.')
        return redirect('logincuarteleros')

def agnadir_servicio(request):
    return render(request, 'cuarteleros/agnadir-servicio.html')

def agnadir_asistencia(request):
    return render(request, 'cuarteleros/agnadir-asistencia.html')

def servicios(request):
    return render(request, 'cuarteleros/servicios.html')

def asistencias(request):
    return render(request, 'cuarteleros/asistencias.html')

def personal(request):
    return render(request, 'cuarteleros/personal-cuartelero.html')

