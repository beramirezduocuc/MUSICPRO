from django.shortcuts import render
from core.models import Producto
#from transbank import Webpay


def medioPago(request):
    return render(request, 'ventas/medioPago.html')

def eleccionTransferencia(request):
    return render(request,'ventas/eleccionTransferencia.html')

def transfExitosa(request):
    return render(request, 'ventas/transfExitosa.html')

def productos(request):
    productos = Producto.objects.all()
    data = { 
        'productos': productos
    }
    return render(request, 'ventas/productos.html', data)


def carrito(request):

    return render(request, 'ventas/carrito.html')


