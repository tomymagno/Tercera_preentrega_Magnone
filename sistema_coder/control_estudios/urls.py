from django.contrib import admin
from django.urls import path

from control_estudios.views import (
    listar_clientes, listar_productos, crear_producto, buscar_producto
)

#Son las URLS especificas de la app.

urlpatterns = [
    path("clientes/", listar_clientes, name="lista_clientes"),
    path("productos/", listar_productos, name="lista_productos"),
    path("crear-producto/", crear_producto, name="crear_producto"),
    path("buscar-productos/", buscar_producto, name="buscar_productos"),

]
