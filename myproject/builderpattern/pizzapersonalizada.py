from constructorpizza import PizzaBuilder
from pizza import Pizza

class PizzaCustomizadaBuilder(PizzaBuilder):

    def __init__(self):
        self.pizza = Pizza()

    def añadir_masa(self):
        opciones_masa = ['fina', 'gruesa']
        while True:
            masa = input('¿Qué masa quieres? fina o gruesa: ')
            if masa.lower() in opciones_masa:
                self.pizza.masa = masa.lower()
                break
            else:
                print('Error: Por favor, ingresa "fina" o "gruesa".')

    def añadir_salsa(self):
        opciones_salsa = ['tomate', 'barbacoa']
        while True:
            salsa = input('¿Qué salsa quieres? tomate o barbacoa: ')
            if salsa.lower() in opciones_salsa:
                self.pizza.salsa = salsa.lower()
                break
            else:
                print('Error: Por favor, ingresa "tomate" o "barbacoa".')

    def añadir_ingredientes_principales(self):
        opciones_ingredientes = ['tomate', 'queso', 'jamon', 'atun', 'champiñones', 'bacon', 'cebolla', 'pollo', 'piña',
                                'aceitunas', 'anchoas', 'maiz', 'salchichas', 'pimiento', 'gambas', 'carne picada', 'huevo']
        while True:
            print("Elige los ingredientes principales para tu pizza:")
            for i, ingrediente in enumerate(opciones_ingredientes, start=1):
                print(f"{i}. {ingrediente}")

            seleccionados = input("Ingresa los números de los ingredientes separados por comas: ")
            
            if seleccionados.replace(',', '').isdigit() and seleccionados:
                numeros_seleccionados = [int(x) for x in seleccionados.split(',')]

                if all(1 <= num <= len(opciones_ingredientes) for num in numeros_seleccionados):
                    ingredientes_seleccionados = [opciones_ingredientes[i - 1] for i in numeros_seleccionados]
                    self.pizza.ingredientes_principales = ingredientes_seleccionados
                    break
                else:
                    print('Error: Ingresa números válidos.')
            else:
                print('Error: Ingresa números válidos y asegúrate de no dejar la entrada vacía.')


    def añadir_coccion(self):
        opciones_coccion = ['al horno', 'a la piedra']
        while True:
            coccion = input('¿Cómo quieres que se cocine? al horno o a la piedra: ')
            if coccion.lower() in opciones_coccion:
                self.pizza.coccion = coccion.lower()
                break
            else:
                print('Error: Por favor, ingresa "al horno" o "a la piedra".')

    def añadir_presentacion(self):
        opciones_presentacion = ['entera', 'en porciones']
        while True:
            presentacion = input('¿Cómo quieres que se presente? entera o en porciones: ')
            if presentacion.lower() in opciones_presentacion:
                self.pizza.presentacion = presentacion.lower()
                break
            else:
                print('Error: Por favor, ingresa "entera" o "en porciones".')

    def añadir_maridaje_recomendado(self):

        bebidas = {
            'cerveza': ['pollo', 'bacon', 'salchichas', 'carne picada', 'huevo', 'queso'],
            'vino blanco': ['gambas', 'atun', 'anchoas', 'queso', 'champiñones'],
            'vino_tinto': ['queso', 'aceitunas', 'tomate', 'maiz', 'champiñones', 'pimiento'],
            'sangria': ['pollo', 'bacon', 'queso', 'huevo', 'atun', 'jamon', 'carne picada'],
            'cocacola': ['huevo', 'queso', 'jamon', 'bacon', 'champiñones', 'pollo', 'pimiento', 'carne picada', 'salchichas'],
            'fanta_naranja': ['aceitunas', 'atun', 'anchoas', 'maiz', 'gambas'],
            'fanta_limon': ['pollo', 'bacon', 'queso', 'salchichas', 'huevo', 'atun', 'jamon', 'carne picada', 'champiñones', 'pimiento'],
            'agua': ['pollo', 'bacon', 'queso', 'salchichas', 'huevo', 'atun', 'jamon', 'carne picada', 'champiñones', 'pimiento']
        }

        ingredientes_pizza = self.pizza.ingredientes_principales

        maridaje_recomendado = None
        max_coincidencias = 0

        for bebida, ingredientes_bebida in bebidas.items():
            coincidencias = len(set(ingredientes_pizza).intersection(ingredientes_bebida))
            if coincidencias > max_coincidencias:
                max_coincidencias = coincidencias
                maridaje_recomendado = bebida

        print(f"El maridaje recomendado para tu pizza es: {maridaje_recomendado}")
        
        while True:
            cambiar_maridaje = input('¿Quieres cambiar el maridaje recomendado? si o no: ')
            if cambiar_maridaje.lower() == 'si':
                nueva_bebida = input('¿Qué bebida quieres? cerveza, vino blanco, vino tinto, sangria, cocacola, fanta_naranja, fanta_limon o agua: ')
                if nueva_bebida.lower() in bebidas.keys():
                    self.pizza.maridaje_recomendado = nueva_bebida.lower()
                    break
                else:
                    print('Error: Por favor, elige una bebida válida.')
            elif cambiar_maridaje.lower() == 'no':
                self.pizza.maridaje_recomendado = maridaje_recomendado
                break
            else:
                print('Error: Por favor, ingresa "si" o "no".')

    def añadir_extra(self):
        opciones_extra = ['si', 'no']
        while True:
            extra = input('¿Quieres bordes rellenos de queso? si o no: ')
            if extra.lower() in opciones_extra:
                self.pizza.extra = 'bordes rellenos de queso' if extra.lower() == 'si' else 'sin bordes rellenos de queso'
                break
            else:
                print('Error: Por favor, ingresa "si" o "no".')