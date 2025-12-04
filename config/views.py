from .models import *
from .forms import ProductoForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .cart import add_to_cart, remove_from_cart, clear_cart, get_cart
# Vista base que renderiza la plantilla base
def base(request):
    return render(request, 'Pages/Base.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # iniciar sesión automáticamente
            return redirect('Home')  # Cambia a la página principal que uses
    else:
        form = UserCreationForm()

    return render(request, 'Pages/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('Home')
    else:
        form = AuthenticationForm()

    return render(request, 'Pages/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('Home')
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
    query = request.GET.get("q")  # Texto que escribe el usuario

    productos = Producto.objects.all()  # Todos los productos

    # Si escribió algo → filtramos
    if query:
        productos = productos.filter(
            Q(nombre__icontains=query) |
            Q(descripcion__icontains=query)
        )

    return render(request, 'Pages/Productos.html', {
        'productos': productos,
        'query': query
    })

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



def buscar_producto(request):
    query = request.GET.get("q")  # nombre del input

    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.none()  # lista vacía

    return render(request, "Catalogo.html", {"productos": productos, "query": query})

def carrito(request):
    cart = request.session.get('carrito', {})
    productos = []
    total = 0

    for product_id, cantidad in cart.items():
        p = Producto.objects.get(id=product_id)
        subtotal = p.precio * cantidad
        total += subtotal
        productos.append({
            'obj': p,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

    return render(request, 'Pages/carrito.html', {
        'items': productos,
        'total': total
    })




def agregar_carrito(request, id):
    carrito = request.session.get('carrito', {})

    id = str(id)  # <-- OBLIGATORIO: guardar como STRING

    carrito[id] = carrito.get(id, 0) + 1

    request.session['carrito'] = carrito
    return redirect('Productos')



def eliminar_carrito(request, id):
    remove_from_cart(request.session, id)
    return redirect('carrito')


def vaciar_carrito(request):
    request.session['carrito'] = {}  # vaciar
    request.session.modified = True  # asegurar que se guarde
    return redirect('carrito')
