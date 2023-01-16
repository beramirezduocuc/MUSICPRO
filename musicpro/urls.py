from django.contrib import admin
from django.urls import path, include
from inicio import views

urlpatterns = [
    path('', views.inicio, name='home'),
    path('admin/', admin.site.urls),
    path('login/', include(('registro.urls', 'login'), namespace='login')),
    path('venta/', include(('venta.urls', 'venta'), namespace='venta')),
    path('inicio/', include(('inicio.urls', 'inicio'), namespace='inicio')),

]
