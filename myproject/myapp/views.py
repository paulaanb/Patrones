# myapp/views.py
from django.shortcuts import render
from .models import MenuItem, Menu
from .builders import PizzaBuilder, MenuBuilder

def create_pizza(request):
    pizza_builder = PizzaBuilder()
    pizza_builder.build_dough("Thin Crust")
    pizza_builder.build_sauce("Tomato")
    pizza_builder.build_toppings(["Cheese", "Mushrooms", "Pepperoni"])
    pizza = pizza_builder.get_pizza()
    return render(request, 'pizza.html', {'pizza': pizza})

def create_menu(request):
    menu_builder = MenuBuilder()
    menu_builder.build_name("Special Combo")
    
    # Get items from the database or create new ones
    pizza_item = MenuItem.objects.get_or_create(code='P1', name='Custom Pizza', price=15.0)[0]
    
    menu_builder.add_item(pizza_item)
    menu_builder.set_discount(2.0)
    
    special_menu = menu_builder.get_menu()
    return render(request, 'menu.html', {'menu': special_menu})
