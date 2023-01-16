from django.shortcuts import render

# Create your views here.
def contacto(request):
    return render(request, 'inicio/contacto.html')

def inicio(request):
    return render(request, 'inicio/inicio.html')