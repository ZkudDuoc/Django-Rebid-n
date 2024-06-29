from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto,Cliente,Empleado
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index_view(request):
    return render(request, "index.html")
def certificacion_view(request):
    return render(request, "Certificacion.html")
def contactanos_view(request):
    return render(request, "Contactanos.html")
def inicio_view(request):
    return render(request, "Inicio.html")

def sobrenosotros_view(request):
    return render(request, "SobreNosotros.html")


#Productos
def listar_view(request):
    productos = Producto.objects.all()
    context = {'productos' : productos}
    return render(request,"Listar.html", {'productos' : productos})

def agregar_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        
        # Crear un nuevo objeto Producto y guardarlo
        Producto.objects.create(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)
        
        # Redirigir a la página de listado de productos
        return HttpResponseRedirect('/Listar/')  # Cambia '/Listar/' por la URL correcta de tu listado de productos
    else:
        return render(request, 'agregar.html')
    

def eliminar_view(request, id):
    producto = get_object_or_404(Producto, pk=id)
    
    if request.method == 'POST':
        # Eliminar el producto
        producto.delete()
        # Redirigir a la página de listado de productos
        return HttpResponseRedirect('listar_view')  # Cambia '/Listar/' por la URL correcta de tu listado de productos
    
    # Renderizar el template de confirmación de eliminación
    return render(request, 'Eliminar.html', {'producto': producto})

#clientes
def listar_cliente_view(request):
    clientes = Cliente.objects.all()
    context = {'clientes' : clientes}
    return render(request,"Listar_cliente.html", {'clientes' : clientes})

def agregar_cliente_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        contraseña = request.POST.get('contraseña')
        
        # Crear un nuevo objeto Producto y guardarlo
        Cliente.objects.create(nombre=nombre, apellido=apellido, email=email, contraseña=contraseña)
        
        # Redirigir a la página de listado de productos
        return HttpResponseRedirect('/Listar_cliente/')  # Cambia '/Listar/' por la URL correcta de tu listado de productos
    else:
        return render(request, 'agregar.html')