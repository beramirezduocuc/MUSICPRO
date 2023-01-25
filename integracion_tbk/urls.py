from django.urls import path
from integracion_tbk import views


app_name = "integracion_tbk"
urlpatterns = [
	path('', views.init, name='init'),
	path('normal_index', views.normal_index, name='normal_index'),
	path('normal_init_transaction', views.normal_init_transaction, name='normal_init_transaction'),
	path('return', views.normal_return_from_webpay, name='normal_return_from_webpay'),
	path('final', views.normal_final, name='normal_final'),
]