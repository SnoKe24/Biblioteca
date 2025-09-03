from django.contrib import admin
from .models import *
from .apps import *

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_per_page = 10


admin.site.register(Producto, ProductoAdmin)
