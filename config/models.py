from django.db import models
from ckeditor.fields import RichTextField

class Productos(models.Model):
    Codigo= models.IntegerField(primary_key=True),
    Nombre= models.TextField(max_length=20),

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    # Nombre del producto, campo obligatorio de texto corto
    nombre = models.CharField(max_length=100, help_text="")
    descripcion = RichTextField(max_length=50, help_text="Descripción del producto", null=True)
    # Precio del producto con dos decimales
    precio = models.DecimalField(max_digits=8, decimal_places=2, help_text="$ Pesos")
    # Campo para subir imagen y almacenarla en carpeta media
    imagen = models.ImageField(upload_to="productos/", null=True, blank=True)
    imagen_url = models.CharField(max_length=255, blank=True, null=True, help_text="Ruta o URL de la imagen del producto")
    # Filtrar por categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos", null=True, blank=True)
    # Fecha y hora de creación automática para ordenar productos por fecha
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['-fecha_creacion']  # Ordenar productos por fecha creación descendente


class Mother(models.Model):
    nombre = models.CharField(max_length=100, help_text="")
    precio = models.DecimalField(max_digits=8, decimal_places=2, help_text="$ Pesos")
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, help_text="")

class Proce():
    nombre = models.CharField(max_length=100, help_text="")
    precio = models.DecimalField(max_digits=8, decimal_places=2, help_text="$ Pesos")
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, help_text="")

class Ram():
    nombre = models.CharField(max_length=100, help_text="")
    precio = models.DecimalField(max_digits=8, decimal_places=2, help_text="$ Pesos")
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, help_text="")

class Mouse():
    nombre = models.CharField(max_length=100, help_text="")
    precio = models.DecimalField(max_digits=8, decimal_places=2, help_text="$ Pesos")
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, help_text="")

class KBoard():
    nombre = models.CharField(max_length=100, help_text="")
    precio = models.DecimalField(max_digits=8, decimal_places=2, help_text="$ Pesos")
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, help_text="")
