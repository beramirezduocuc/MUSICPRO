from rest_framework import serializers
from core.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('ID_producto', 'Categoria', 'Nombre', 'Modelo', 'Precio', 'Cantidad')