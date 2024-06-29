from django.contrib import admin
from django.urls import path
from tiendaAgua.views import index_view, eliminar_view, agregar_view, certificacion_view, contactanos_view, inicio_view, Registro_view, listar_view, sobrenosotros_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('Certificacion/', certificacion_view, name='Certificacion'),
    path('Contactanos/', contactanos_view, name='Contactanos'),
    path('Inicio/', inicio_view, name='Inicio'),
    path('Sobrenosotros/', sobrenosotros_view, name='SobreNosotros'),
    path('Registro/', Registro_view, name='Registro'),
    path('Listar/', listar_view, name= 'listado_producto'),
    path('Agregar/', agregar_view,  name='agregar_listar'),
    path('Eliminar/<int:id>/', eliminar_view, name='eliminar_producto')
]

