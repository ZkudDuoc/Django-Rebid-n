from django.contrib import admin

# Register your models here.

from .models import Cliente, Empleado, Producto

admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Producto)
