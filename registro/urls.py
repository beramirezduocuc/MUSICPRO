from django.urls import path 
from . import views as v_registro

urlpatterns = [
path('login/', v_registro.login, name='login'),
path('registro/', v_registro.registro, name='registro'),
path('terminos/', v_registro.ToS, name='ToS'),

]