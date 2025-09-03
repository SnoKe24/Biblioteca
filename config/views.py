from .models import Producto
from .forms import ProductoForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
# Vista base que renderiza la plantilla base
def base(request):
    return render(request, 'Pages/Base.html')

# Vista para la página principal (Home)
def home(request):
    ultimos_productos_desc = Producto.objects.order_by('-id')[:5]
    ultimos_productos = list(reversed(ultimos_productos_desc))
    # Agregar imagen_url si no está definido, usar imagen.url si existe
    for producto in ultimos_productos:
        if not producto.imagen_url and producto.imagen:
            producto.imagen_url = producto.imagen.url
    return render(request, 'Pages/Home.html', {'ultimos_productos': ultimos_productos})

def catalogo(request):
    # Obtener hasta 20 productos con imagen para la galería
    productos = Producto.objects.filter(imagen__isnull=False).exclude(imagen='')[:20]
    return render(request, 'Pages/Catalogo.html', {'productos': productos})

# Vista para la página "Acerca de Nosotros"
def about(request):
    return render(request, 'Pages/About.html')

# Vista para listar todos los productos con opciones CRUD
def productos(request):
    productos = Producto.objects.all()
    return render(request, 'Pages/Productos.html', {'productos': productos})

# Vista para crear un nuevo producto (registro oculto)
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Productos')
    else:
        form = ProductoForm()
    return render(request, 'Pages/crear_producto.html', {'form': form})

# Vista para editar un producto existente
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "Se ha modificado Correctamente")
            return redirect('Productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'Pages/editar_producto.html', {'form': form, 'producto': producto})

# Vista para eliminar un producto
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, "Eliminado con Exito")
        return redirect('Productos')
    return render(request, 'Pages/eliminar_producto.html', {'producto': producto})