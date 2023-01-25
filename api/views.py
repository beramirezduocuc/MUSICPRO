from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Producto
from .serializers import ProductoSerializer
from django.shortcuts import redirect
from transbank import *


#API 1, busca productos en la base de datos según su nombre.
@api_view(['GET'])
def buscar_producto(request, nombre):
    productos = Producto.objects.filter(Nombre__icontains=nombre)
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)



