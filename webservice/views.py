from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, 'views/welcome.html')

def register(request):
    return render(request, 'views/register.html')

def catalog(request):
    return render(request, 'views/catalog.html')

def show_register(request):
    return render(request, "register.html")