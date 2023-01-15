from django.contrib import admin
from django.urls import path
from registro import views as v_registro
from venta import views as v_venta
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', v_registro.login, name='login'),
    path('registro/', v_registro.registro, name='registro'),
    path('terminos/', v_registro.ToS, name='ToS'),

    path('', views.inicio, name='inicio'),

    path('mediodepago/', v_venta.medioPago, name='medioPago'),
    path('transferencia/', v_venta.eleccionTransferencia, name='eleccionTransferencia'),
    path('transfExitosa/', v_venta.transfExitosa, name='tExitosa'),
    path('productos/', v_venta.productos, name='productos'),
    path('carrito/', v_venta.carrito, name='carrito'),
]
