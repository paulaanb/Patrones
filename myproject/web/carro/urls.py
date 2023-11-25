from django.urls import path

from . import views

app_name = 'carro'

urlpatterns = [

    path('agregar/<int:combo_id>/', views.agregar_combo, name='agregar'),
    path('eliminar/<int:combo_id>/', views.eliminar_combo, name='eliminar'),
    path('restar/<int:combo_id>/', views.restar_combo, name='restar'),
    path('limpiar/', views.limpiar_carro, name='limpiar'),

]
