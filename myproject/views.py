from django.db import transaction
from django.shortcuts import render, redirect
from models import Combo
import pandas as pd
import csv
from django.http import HttpResponse

# Create your views here.
@transaction.atomic
def menu(request):
    combos = Combo.objects.all()
    return render(request, 'menu/menu.html', {'combos':combos})

def ver_pedido_csv(request):
    # Nombre del archivo CSV
    csv_file_name = 'pedido.csv'

    try:
        # Abre el archivo CSV en modo lectura
        with open(csv_file_name, 'r') as csvfile:
            # Lee el contenido del archivo
            csv_content = csvfile.read()
    except FileNotFoundError:
        return HttpResponse("El archivo CSV no se encuentra.")

    # Renderiza el contenido CSV en una plantilla HTML
    return render(request, 'ver_pedido_csv.html', {'csv_content': csv_content})


def guardar_pedido_en_csv(request):
    # Obtener el carrito de la sesión
    carro = request.session.get('carro', {})

    # Verificar si hay elementos en el carrito
    if not carro:
        return HttpResponse("El carrito está vacío.")

    # Nombre del archivo CSV
    csv_file_name = 'pedido.csv'

    # Abrir el archivo CSV en modo escritura
    with open(csv_file_name, 'w', newline='') as csvfile:
        # Definir los encabezados del CSV
        fieldnames = ['Combo ID', 'Nombre', 'Precio']

        # Crear el objeto escritor CSV
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Escribir los encabezados al archivo
        writer.writeheader()

        # Escribir cada elemento del carrito al archivo
        for combo_id, combo_data in carro.items():
            writer.writerow({
                'Combo ID': combo_id,
                'Nombre': combo_data['nombre'],
                'Precio': combo_data['precio']
                # Agregar más campos según sea necesario
            })

    return HttpResponse(f"Carrito guardado exitosamente en {csv_file_name}.")