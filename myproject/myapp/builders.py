# myapp/builders.py
class PizzaBuilder:
    def __init__(self):
        self.pizza = MenuItem()

    def build_dough(self, dough_type):
        self.pizza.name = f"{dough_type} Pizza"
        self.pizza.price += 5.0

    def build_sauce(self, sauce_type):
        self.pizza.name += f" with {sauce_type} Sauce"
        self.pizza.price += 2.0

    def build_toppings(self, toppings):
        for topping in toppings:
            self.pizza.name += f", {topping}"
            self.pizza.price += 1.0

    def get_pizza(self):
        return self.pizza


class MenuBuilder:
    def __init__(self):
        self.menu = Menu()

    def build_name(self, name):
        self.menu.name = name

    def add_item(self, item):
        self.menu.items.add(item)

    def set_discount(self, discount):
        self.menu.discount = discount

    def get_menu(self):
        return self.menu
