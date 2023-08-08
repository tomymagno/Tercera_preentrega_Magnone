from django.db import models

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=64)
    precio = models.IntegerField()

    def __str__(self):
        return f"{self.nombre_producto}, {self.precio}"
    
class Cliente(models.Model):
    apellido = models.CharField(max_length=256)
    nombre = models.CharField(max_length=256)
    email = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    dni = models.CharField(max_length=32)
    fecha_nacimiento = models.DateField(null=True)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
    
class Proveedores(models.Model):
    titular = models.CharField(max_length=256)
    empresa = models.CharField(max_length=256)
    email_empresa = models.EmailField(blank=True)
    email_titular = models.EmailField(blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    fecha_creacion = models.DateField(null=True, blank=True)
    tipo_productos = models.TextField(blank=True)

    def __str__(self):
        return f"{self.empresa}, {self.titular}"

'''
class Entregable(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    fecha_entrega = models.DateTimeField(auto_now_add=True)
    esta_aprobado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
'''