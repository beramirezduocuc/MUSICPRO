from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

def login(request):
    return render(request, "registro/login.html")

def registro(request):
    return render(request, "registro/registro.html")

def ToS(request):
    return render(request, "registro/ToS.html")


