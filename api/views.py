from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Producto
from .serializers import ProductoSerializer
#API 1, busca productos en la base de datos según su nombre.
#Para consultar a la api en postman: http://127.0.0.1:8000/productos/buscar/Bajo    
@api_view(['GET'])
def buscar_producto(request, nombre):
    productos = Producto.objects.filter(Nombre__icontains=nombre)
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)



