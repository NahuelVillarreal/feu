from django.shortcuts import render

# Create your views here.

def standby(request):
    return render(request, "standby.html")