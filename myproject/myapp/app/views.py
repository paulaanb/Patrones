from django.shortcuts import render, HttpResponse, redirect
from .form import PizzaBuilderForm
from .models import Pizza
from .storage import PizzaCSV
import csv
import pandas as pd
from carro.carro import Carro

def home(request):
    carro = Carro(request)
    return render(request, "app/home.html")

def pedir(request):
    masa = ""  
    salsa = ""
    ingredientes_principales = ""
    coccion = ""
    presentacion = ""
    maridaje_recomendado = ""
    extra = ""

    if request.method == 'POST':
        form = PizzaBuilderForm(request.POST)
        if form.is_valid():
            masa=form.cleaned_data['masa']
            salsa=form.cleaned_data['salsa']
            ingredientes_principales=form.cleaned_data['ingredientes_principales']
            coccion=form.cleaned_data['coccion']
            presentacion=form.cleaned_data['presentacion']
            maridaje_recomendado=form.cleaned_data['maridaje_recomendado']
            extra=form.cleaned_data['extra_bordes_queso']

        pizza_order= Pizza(
            masa=masa,
            salsa=salsa,
            ingredientes_principales=ingredientes_principales,
            coccion=coccion,
            presentacion=presentacion,
            maridaje_recomendado=maridaje_recomendado,
            extra=extra
        )
        pizza_order.save()
   
        csv_file_name = 'pizza.csv'
        pizza_csv = PizzaCSV(csv_file_name)
        pizza_csv.write_pizza_to_csv(pizza_order)
        return render(request,'app/home.html')
      
    
    else:
        form = PizzaBuilderForm()

    return render(request, "app/pedir.html", {'form': form})



def ver_csv(request):
    csv_file_name = 'pizza.csv' 
    df = pd.read_csv(csv_file_name)


    table_html = df.to_html(classes='table table-striped')

    return render(request, 'app/ver_csv.html', {'table_html': table_html})


def resumen_pedido(request):
    if request.method == 'POST':
        form= PizzaBuilderForm(request.POST)
        if form.is_valid():
            masa=form.cleaned_data['masa']
            salsa=form.cleaned_data['salsa']
            ingredientes_principales=form.cleaned_data['ingredientes_principales']
            coccion=form.cleaned_data['coccion']
            presentacion=form.cleaned_data['presentacion']
            maridaje_recomendado=form.cleaned_data['maridaje_recomendado']
            extra=form.cleaned_data['extra_bordes_queso']

            return render(request, 'app/resumen_pedido.html', {'masa': masa, 'salsa': salsa, 'ingredientes_principales': ingredientes_principales, 'coccion': coccion, 'presentacion': presentacion, 'maridaje_recomendado': maridaje_recomendado, 'extra': extra, 'form': form})
        
    return redirect ('pedir')





def confirmar_modificar_pedido(request):
    print(request.POST)
    if request.method == 'POST':
        decision = request.POST.get('decision')

        if decision == 'confirmar':
    
            masa = request.POST.get('masa')
            salsa = request.POST.get('salsa')
            ingredientes_principales = request.POST.get('ingredientes_principales')
            coccion = request.POST.get('coccion')
            presentacion = request.POST.get('presentacion')
            maridaje_recomendado = request.POST.get('maridaje_recomendado')
            extra = request.POST.get('extra')


            csv_file_name = 'pizza.csv'
            with open(csv_file_name, mode='a', newline='') as file:
                writer = csv.writer(file)
                if file.tell() == 0: 
                    writer.writerow(['Masa', 'Salsa', 'Ingredientes Principales', 'Cocción', 'Presentación', 'Maridaje Recomendado', 'Extra'])
                writer.writerow([masa, salsa, ingredientes_principales, coccion, presentacion, maridaje_recomendado, extra])

            return redirect('home')
        
        elif decision == 'modificar':
            return redirect('pedir')

    return HttpResponse("Invalid decision or appropriate response")


