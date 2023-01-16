from django.urls import path
from . import views as v_inicio

urlpatterns = [
path('contacto/', v_inicio.contacto, name="contacto"),
path('inicio/', v_inicio.inicio, name="inicio"),
]