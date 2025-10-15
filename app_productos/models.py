# app_productos/models.py

from django.db import models

class Producto(models.Model):
    # Django creará automáticamente el campo ID (id)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50) 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    categoria = models.CharField(max_length=50) # Ejemplo: "Pasteles", "Galletas", "Panadería"
    unidad_medida = models.CharField(max_length=10, default='kg') # Por defecto 'kg'

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre