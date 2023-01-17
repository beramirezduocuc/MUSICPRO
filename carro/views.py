from django.shortcuts import render, redirect
from .carro import Carro
from core.models import Producto

def agregar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(ID_producto=producto_id)
    carro.agregar(producto=producto)
    return redirect("venta:productos")

def eliminar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("venta:carrito")


def restar_producto(request, producto_id):

    carro=Carro(request)

    producto=Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("venta:carrito")

def limpiar_carro(request, producto_id):

    carro=Carro(request)

    carro.limpiar_carro()
    return redirect("venta:carrito")