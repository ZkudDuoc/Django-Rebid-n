from django.contrib import admin
from django.urls import path
from tiendaAgua.views import index_view, Exito_view, Recui_view, listar_cliente_view,eliminar_cliente_view, modificar_empleado_view, eliminar_empleado_view,  modificar_cliente_view, listar_empleados_view, agregar_empleado_view,  eliminar_view, agregar_cliente_view, agregar_view, certificacion_view, Login_view, contactanos_view, inicio_view, Registro_view, listar_view, sobrenosotros_view, modificar_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('Certificacion/', certificacion_view, name='Certificacion'),
    path('Contactanos/', contactanos_view, name='Contactanos'),
    path('Inicio/', inicio_view, name='Inicio'),
    path('Login/', Login_view, name='Login'),
    path('Sobrenosotros/', sobrenosotros_view, name='SobreNosotros'),
    path('Registro/', Registro_view, name='Registro'),
    path('Recui/', Recui_view, name='Recui'),
    path('Exito/', Exito_view, name='Exito'),
    path('Listar/', listar_view, name= 'listado_producto'),
    path('Agregar/', agregar_view,  name='agregar_listar'),
    path('Eliminar/<int:id>/', eliminar_view, name='eliminar_producto'),
    path('modificar/<int:id>/', modificar_view, name='modificar_producto'),
    path('Listar_cliente/', listar_cliente_view, name='listar_clientes'),
    path('agregar_cliente/',agregar_cliente_view, name = 'agregar_cliente'),
    path('eliminar_cliente/<int:id>/',eliminar_cliente_view, name = 'eliminar_cliente'),
    path('modificar_cliente/<int:id>/', modificar_cliente_view, name='modificar_cliente'),
    path('listar_empleados/', listar_empleados_view, name='listar_empleados'),
    path('agregar_empleado/', agregar_empleado_view, name='agregar_empleado'),
    path('modificar_empleado/<int:id>/', modificar_empleado_view, name='modificar_empleado'),
    path('eliminar_empleado/<int:id>/', eliminar_empleado_view, name='eliminar_empleado'),
]

