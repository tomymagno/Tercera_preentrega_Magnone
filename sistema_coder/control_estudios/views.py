from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q


from control_estudios.models import Producto, Cliente
from control_estudios.forms import ProductoFormulario

def listar_clientes(request):
    contexto = {
        "clientes": Cliente.objects.all(),
    }
    HttpResponse = render(
        request=request,
        template_name='control_estudios/lista_clientes.html',
        context=contexto,
    )
    return HttpResponse

def listar_productos(request):
    contexto = {
        "productos": Producto.objects.all(),
    }
    HttpResponse = render(
        request=request,
        template_name='control_estudios/lista_productos.html',
        context=contexto,
    )
    return HttpResponse

def crear_producto(request):
    if request.method == "POST":
        formulario = ProductoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre_producto = data["nombre_producto"]
            precio = data["precio"]
            producto = Producto(nombre_producto=nombre_producto, precio=precio)  # lo crean solo en RAM
            producto.save()  # Lo guardan en la Base de datos

            # Redirecciono al usuario a la lista de cursos
            url_exitosa = reverse('lista_productos')  # estudios/cursos/
            return redirect(url_exitosa)
    else:  # GET
        formulario = ProductoFormulario()
    http_response = render(
        request=request,
        template_name='control_estudios/formulario_producto.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_productos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        cursos = Producto.objects.filter(
            Q(nombre=busqueda) | Q(producto__contains=busqueda)
            )
        contexto = {
            "productos": productos,
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_productos.html',
            context=contexto,
        )
        return http_response
