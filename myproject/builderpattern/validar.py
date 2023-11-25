from constructorpizza import PizzaBuilder
from pizza import Pizza
from directorpizza import PizzaDirector
from pizzapersonalizada import PizzaCustomizadaBuilder
from crearcsv import PizzaCSV
class PizzaValidator:
    def __init__(self, builder):
        self.builder = builder
        self.pizza = None

    def set_pizza(self, pizza):
        self.pizza = pizza

    def mostrar_resumen(self):
        if self.pizza:
            print("Resumen de selecciones:")
            print(f"Masa: {self.pizza.masa}")
            print(f"Salsa: {self.pizza.salsa}")
            print(f"Ingredientes Principales: {', '.join(self.pizza.ingredientes_principales)}")
            print(f"Cocción: {self.pizza.coccion}")
            print(f"Presentación: {self.pizza.presentacion}")
            print(f"Maridaje: {self.pizza.maridaje_recomendado}")
            print(f"Extras: {self.pizza.extra}")
        else:
            print("No hay una pizza configurada para mostrar un resumen.")

    def verificar_pizza(self):
        self.mostrar_resumen()
        if self.pizza:
            print("¿Estás satisfecho con las modificaciones realizadas en la pizza?")
            confirmacion = input('Responde "si" para confirmar la pizza o "no" para seguir modificando: ')
            if confirmacion.lower() == 'si':
                print("Pizza confirmada. ¡Gracias por tu pedido!")
                return True
            elif confirmacion.lower() == 'no':
                self.modificar_selecciones()
                return self.verificar_pizza()
            else:
                print("Respuesta no válida. Debes responder 'si' o 'no.")
                return self.verificar_pizza()
        else:
            print("No hay una pizza configurada para verificar.")

    def modificar_selecciones(self):
        if self.pizza:
            print("Modifica tus selecciones antes de confirmar:")
            self.builder = PizzaCustomizadaBuilder()
            director = PizzaDirector()
            director.builder = self.builder
            director.crear_pizza()
            self.set_pizza(director.get_pizza())
        else:
            print("No hay una pizza configurada para modificar.")