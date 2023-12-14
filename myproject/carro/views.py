from django.shortcuts import render
from carro import Carro
from models import *
from composite import Combo


from django.shortcuts import redirect


def agregar_combo(request, combo_id):
    carro = Carro(request)
    combo = Combo.objects.get(id=combo_id)
    carro.agregar(combo=combo)
    return redirect("menu")

def eliminar_combo(request, combo_id):
    carro = Carro(request)
    combo = Combo.objects.get(id=combo_id)
    carro.eliminar(combo=combo)
    return redirect("menu")

def restar_combo(request, combo_id):
    carro = Carro(request)
    combo = Combo.objects.get(id=combo_id)
    carro.restar_producto(combo=combo)
    return redirect("menu")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("menu")