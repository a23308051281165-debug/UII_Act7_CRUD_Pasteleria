# app_productos/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

# ==================================
# 1. LISTAR / READ ALL (index)
# ==================================
def index_productos(request):
    """Muestra la lista de todos los productos."""
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})

# ==================================
# 2. AGREGAR / CREATE
# ==================================
def agregar_producto(request):
    """Maneja la creación de un nuevo producto."""
    if request.method == 'POST':
        Producto.objects.create(
            nombre = request.POST['nombre'],
            tipo = request.POST['tipo'],
            precio = request.POST['precio'],
            stock = request.POST['stock'],
            categoria = request.POST['categoria'],
            unidad_medida = request.POST['unidad_medida']
        )
        return redirect('productos_inicio') 
        
    return render(request, 'productos/agregar_producto.html')

# ==================================
# 3. EDITAR / UPDATE
# ==================================
def editar_producto(request, id):
    """Maneja la edición de un producto existente."""
    producto = get_object_or_404(Producto, id=id) 
    
    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.tipo = request.POST['tipo']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        producto.categoria = request.POST['categoria']
        producto.unidad_medida = request.POST['unidad_medida']
        producto.save() 
        
        return redirect('productos_inicio')
    
    return render(request, 'productos/editar_producto.html', {'producto': producto})

# ==================================
# 4. BORRAR / DELETE
# ==================================
def borrar_producto(request, id):
    """Maneja la eliminación de un producto."""
    producto = get_object_or_404(Producto, id=id)
    
    if request.method == 'POST':
        producto.delete()
        return redirect('productos_inicio')
        
    return render(request, 'productos/borrar_producto.html', {'producto': producto})