from django.contrib import admin
from django.urls import path
from registro import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('terminos/', views.ToS, name='ToS'),
    path('', views.inicio, name='inicio'),
    path('mediodepago/', views.medioPago, name='medioPago'),
]
