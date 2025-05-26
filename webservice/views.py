from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
def welcome(request):
    return render(request, 'views/welcome.html')

def register(request):
    return render(request, 'views/register.html')

def catalog(request):
    return render(request, 'views/catalog.html')

def show_register(request):
    return render(request, "register.html")

@api_view(['POST'])
def login_api(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email or not password:
        return Response({'error': 'Email y contraseña son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    user_auth = authenticate(username=user.username, password=password)
    if user_auth is None:
        return Response({'error': 'Contraseña incorrecta'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'message': f'Bienvenido, {user.username}'}, status=status.HTTP_200_OK)