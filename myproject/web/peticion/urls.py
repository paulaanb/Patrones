from django.urls import path

from . import views

urlpatterns = [
    path('',views.procesar_peticion, name='procesar_peticion'),
]