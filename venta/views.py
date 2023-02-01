from django.shortcuts import render, redirect
from core.models import Producto
import random
from django.shortcuts import render
import json
import requests
from django.http import HttpResponseRedirect,HttpResponse


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

from django.http import HttpResponse

import json
import random
import requests

"""
def crearTransaccion(request):

    amount = request.POST.get('amount')
    buy_order = random.randint(100000, 999999)
    session_id = random.randint(100000, 999999)
    url_post = "https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/"
    data = {
        "amount": amount,
        "buy_order": buy_order,
        "session_id": session_id,
        "return_url": "http://127.0.0.1:8000/venta/transbank/"
    }
    headers = { 
                "Tbk-Api-Key-Id":"597055555532",
                "Tbk-Api-Key-Secret": "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C",
                "Content-Type": "application/json", 
                }
    response_post = requests.post(url_post, data=json.dumps(data), headers=headers)
    token = response_post.json()['token']
    url_get = f'https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions/{token}'
    response_get = requests.get(url_get, headers=headers)
    transaccion_data = response_get.json()
    return render(request, 'ventas/transbank.html', {"transaccion_data": transaccion_data})
"""