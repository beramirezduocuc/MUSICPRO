from django.shortcuts import render

def login(request):
    return render(request, "registro/login.html")

def registro(request):
    return render(request, "registro/registro.html")

def ToS(request):
    return render(request, "registro/ToS.html")

def inicio(request):
    return render(request, "core/inicio.html")    

def medioPago(request):
    return render(request, 'ventas/medioPago.html')