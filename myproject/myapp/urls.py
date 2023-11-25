# myapp/urls.py
from django.urls import path
from .views import create_pizza, create_menu

urlpatterns = [
    path('create_pizza/', create_pizza, name='create_pizza'),
    path('create_menu/', create_menu, name='create_menu'),
]
