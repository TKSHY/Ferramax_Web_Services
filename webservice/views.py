import json
import mercadopago
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto



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