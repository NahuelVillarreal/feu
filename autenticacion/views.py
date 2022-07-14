from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def autenticacion(request):
    pass

def logear(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    elif request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            usuario = authenticate(matricula = nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
        else:
            messages.error(request, 'Información incorrecta.')
            return redirect('login')

    form = AuthenticationForm()
    return render(request, 'login/login.html', {'form':form})


def cerrar_sesion(request):
    logout(request)
    return redirect('login')