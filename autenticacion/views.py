from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from usuarios.models import Personal

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

def change_pass(request):
    if not request.user.is_authenticated:
        return redirect('login')
    elif request.method == "POST":
        cont = request.POST["newpass"]
        newcont = request.POST["newpassconfirm"]
        if cont == newcont:
            u = Personal.objects.get(matricula=request.user.matricula)
            u.set_password(cont)
            u.save()
            messages.success(request, "Contraseña cambiada correctamente")
            usuario = authenticate(matricula = request.user.matricula, password=cont)
            login(request, usuario)
            return redirect('perfil')
        else:
            messages.error(request, "Contraseñas no coinciden")
    return render(request, 'login/change-pass.html')