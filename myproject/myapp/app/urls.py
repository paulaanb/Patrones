from django.urls import path
from app import views


urlpatterns = [
    path("", views.home, name="home"),
    path("pedir/", views.pedir, name="pedir"),
    path("ver_csv/", views.ver_csv, name="ver_csv"),
    path('resumen_pedido/', views.resumen_pedido, name='resumen_pedido'),
    path('confirmar_modificar_pedido/', views.confirmar_modificar_pedido, name='confirmar_modificar_pedido'),
    
    


]