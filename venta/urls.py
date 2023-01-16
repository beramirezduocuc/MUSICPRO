from . import views as v_venta
from django.urls import path

urlpatterns = [
path('mediodepago/', v_venta.medioPago, name='medioPago'),
path('transferencia/', v_venta.eleccionTransferencia, name='eleccionTransferencia'),
path('transfExitosa/', v_venta.transfExitosa, name='tExitosa'),
path('productos/', v_venta.productos, name='productos'),
path('carrito/', v_venta.carrito, name='carrito'),

]