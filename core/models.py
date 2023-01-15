from django.db import models


class Tipos_Empleados(models.Model):
    ID_tipo_emp = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)

   
class Empleado(models.Model):
    ID_empleado = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Correo = models.CharField(max_length=30)
    Clave = models.CharField(max_length=30)
    ID_tipo_emp = models.ForeignKey(Tipos_Empleados, on_delete=models.CASCADE)


class Cliente(models.Model):
    ID_cliente = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Apellido = models.CharField(max_length=30)
    Correo = models.CharField(max_length=30)
    Clave = models.CharField(max_length=30)
    Ubicacion = models.CharField(max_length=30)

class Estado_Compras(models.Model):
    ID_estado_compras = models.AutoField(primary_key=True)
    Estado = models.CharField(max_length=30)

class Ventas(models.Model):
    ID_ventas = models.AutoField(primary_key=True)
    Precio = models.IntegerField()
    Producto_vendidos = models.IntegerField()
    Fecha = models.DateField(blank=False, null=False)
    ID_estado_compras = models.ForeignKey(Estado_Compras, on_delete=models.CASCADE)


class Devoluciones(models.Model):
    ID_devoluciones = models.AutoField(primary_key=True)
    Nombre_Producto = models.CharField(max_length=30)
    Fecha = models.DateField(blank=False, null=False)
    ID_Ventas = models.ForeignKey(Ventas, on_delete=models.CASCADE)

class Categoria(models.Model):
    ID_categoria = models.AutoField(primary_key=True)
    Nombre_categoria = models.CharField(max_length=30)


class Clase(models.Model):
    ID_compras = models.AutoField(primary_key=True)
    Nombre_clase = models.CharField(max_length=30)
    ID_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


class Producto(models.Model):
    ID_producto = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Categoria = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=40)
    Modelo = models.CharField(max_length=30)
    Precio = models.IntegerField()
    Cantidad = models.IntegerField()
    ID_Clase = models.ForeignKey(Clase, on_delete=models.CASCADE)


class Tienda(models.Model):
    ID_tienda = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Ubicacion = models.CharField(max_length=30)
    ID_tipo_empleado = models.ForeignKey(Tipos_Empleados, on_delete=models.CASCADE)
    ID_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    ID_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)






