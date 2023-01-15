from django.shortcuts import render

def medioPago(request):
    return render(request, 'ventas/medioPago.html')

def eleccionTransferencia(request):
    return render(request,'ventas/eleccionTransferencia.html')

def transfExitosa(request):
    return render(request, 'ventas/transfExitosa.html')

def productos(request):
    return render(request, 'ventas/productos.html')

def carrito(request):
    return render(request, 'ventas/carrito.html')
