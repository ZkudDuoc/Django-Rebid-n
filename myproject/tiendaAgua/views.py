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
def Registro_view(request):
    return render(request, "Registro.html")    
def sobrenosotros_view(request):
    return render(request, "SobreNosotros.html")
def Login_view(request):
    return render(request, "Login.html")
def Recui_view(request):
    return render(request, "recui.html")
def Exito_view(request):
    return render(request, "Exito.html")  
def listar_view(request):
    productos = Producto.objects.all()
    context = {'productos' : productos}
    return render(request,"Listar.html", {'productos' : productos})   

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
        return HttpResponseRedirect('/Listar/')

def modificar_view(request, id):
    producto = get_object_or_404(Producto, pk=id)
    
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        stock = request.POST.get('stock')
        
        # Actualizar el producto existente con los nuevos datos
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.precio = precio
        producto.stock = stock
        producto.save()
        
        # Redirigir a la página de listado de productos después de modificar
        return HttpResponseRedirect('/Listar/')  # Cambiar '/Listar/' por la URL correcta
        
    return render(request, 'modificar.html', {'producto': producto})


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
        return render(request, 'agregar_cliente.html')
    
def eliminar_cliente_view(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    
    if request.method == 'POST':
        # Eliminar el cliente
        cliente.delete()
        # Redirigir a la página de listado de clientes
        return HttpResponseRedirect('/Listar_cliente/')  # Asegúrate de cambiar '/Listar_cliente/' por la URL correcta
    
    # Renderizar el template de confirmación de eliminación
    return render(request, 'Eliminar_cliente.html', {'cliente': cliente})

def modificar_cliente_view(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    
    if request.method == 'POST':
        # Actualizar los campos del cliente con los datos del formulario
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.email = request.POST.get('email')
        cliente.contraseña = request.POST.get('contraseña')
        cliente.save()
        
        return redirect('listar_clientes')  # Redirige a la página de listado de clientes después de modificar
    
    return render(request, 'modificar_cliente.html', {'cliente': cliente})

#Empleado
def listar_empleados_view(request):
    empleados = Empleado.objects.all()
    return render(request, 'listar_empleados.html', {'empleados': empleados})

def agregar_empleado_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        contraseña = request.POST.get('contraseña')
        cargo = request.POST.get('cargo')
        
        Empleado.objects.create(nombre=nombre, apellido=apellido, email=email, contraseña=contraseña, cargo=cargo)
        
        return HttpResponseRedirect('/listar_empleados/')  # Redirige a la página de listado de empleados
    
    return render(request, 'agregar_empleado.html')

def modificar_empleado_view(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        contraseña = request.POST.get('contraseña')
        cargo = request.POST.get('cargo')
        
        empleado.nombre = nombre
        empleado.apellido = apellido
        empleado.email = email
        empleado.contraseña = contraseña
        empleado.cargo = cargo
        empleado.save()
        
        return redirect('listar_empleados')  # Redirige a la página de listado de empleados después de modificar
    
    return render(request, 'modificar_empleado.html', {'empleado': empleado})

def eliminar_empleado_view(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    
    if request.method == 'POST':
        empleado.delete()
        return redirect('listar_empleados')  # Redirige a la página de listado de empleados después de eliminar
    
    return render(request, 'eliminar_empleado.html', {'empleado': empleado})