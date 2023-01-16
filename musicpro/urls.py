from django.contrib import admin
from django.urls import path, include
from inicio import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.inicio, name='home'),
    path('admin/', admin.site.urls),
    path('login/', include(('registro.urls', 'login'), namespace='login')),
    path('venta/', include(('venta.urls', 'venta'), namespace='venta')),
    path('inicio/', include(('inicio.urls', 'inicio'), namespace='inicio')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)