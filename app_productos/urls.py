# app_productos/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # READ (Listar Productos)
    path('', views.index_productos, name='productos_inicio'), 
    
    # CREATE (Agregar Producto)
    path('agregar/', views.agregar_producto, name='agregar_producto'), 
    
    # UPDATE (Editar Producto)
    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),
    
    # DELETE (Borrar Producto)
    path('borrar/<int:id>/', views.borrar_producto, name='borrar_producto'),
]