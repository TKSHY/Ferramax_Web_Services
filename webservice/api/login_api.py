from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get("email")
            password = data.get("password")

            from django.contrib.auth.models import User
            try:
                user = User.objects.get(email=email)
                username = user.username
            except User.DoesNotExist:
                return JsonResponse({"error": "Usuario no existe"}, status=404)

            user = authenticate(username=username, password=password)
            if user is not None:
                return JsonResponse({"message": "Inicio de sesión exitoso", "username": username}, status=200)
            else:
                return JsonResponse({"error": "Contraseña incorrecta"}, status=401)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)
