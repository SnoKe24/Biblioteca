from django.urls import path
from .views import home, catalogo, about, productos, base, crear_producto, editar_producto, eliminar_producto
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),

    # --- Registro / Login / Logout ---
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    path('', base, name="Base"),
    path('Home/', home, name="Home"),
    path('About/', about, name="About"),
    path('Catalogo/', catalogo, name="Catalogo"),
    path("Productos/", productos, name="Productos"),
    path("buscar/", views.buscar_producto, name="buscar_producto"),
    #CRUD de productos separados
    path('Productos/crear/', crear_producto, name="crear_producto"),
    path('Productos/editar/<int:producto_id>/', editar_producto, name="editar_producto"),
    path('Productos/Eliminar/<int:producto_id>/', eliminar_producto, name="eliminar_producto")
]