from django.urls import path
from webservice import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('catalog/', views.catalog, name='catalog'),
]