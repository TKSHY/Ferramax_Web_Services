import json
import mercadopago
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render

# Vista de bienvenida
def welcome(request):
    productos = Producto.objects.all()
    return render(request, 'views/welcome.html', {'productos': productos})

# Vista del formulario de registro
def register(request):
    return render(request, 'views/register.html')

# Vista del catálogo general
def catalog(request):
    return render(request, 'views/catalog.html')

# Mostrar formulario de registro (otra versión, si aplica)
def show_register(request):
    return render(request, "register.html")