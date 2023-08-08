from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    saludo = "Hola querido usuario"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def inicio(request):
        contexto={
            "profesor": "Pedro",
            "tutores": ["Mariano", "Ariel"],
            "comision": 55350,
        }
        http_response = render(
        request=request,
        template_name="inicio.html",
        context=contexto,
        )
        return http_response

