from django.urls import path
from webservice import views
from webservice.api.register_api import register_user
from .views import login_api

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('catalog/', views.catalog, name='catalog'),
    path("api/register/", register_user, name="register_user"),
    path('api/login/', login_api, name='login_api'),
]