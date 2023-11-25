from abc import ABC, abstractmethod

class ComponentMenu(ABC):

    @abstractmethod
    def mostrar(self):
        pass

class Pizza(ComponentMenu):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


    def mostrar(self):
        print(f'Pizza: {self.nombre} - Precio: {self.precio}')


class Bebida(ComponentMenu):

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f'Bebida: {self.nombre} - Precio: {self.precio}')

class Postre(ComponentMenu):
    
        def __init__(self, nombre, precio):
            self.nombre = nombre
            self.precio = precio
    
        def mostrar(self):
            print(f'Postre: {self.nombre} - Precio: {self.precio}')


class Entrante(ComponentMenu):
        
            def __init__(self, nombre, precio):
                self.nombre = nombre
                self.precio = precio
        
            def mostrar(self):
                print(f'Entrante: {self.nombre} - Precio: {self.precio}')


class Combo(ComponentMenu):

    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self, elemento):
        self.elementos.remove(elemento)
    
    def mostrar(self):
        print(f'Combo: {self.nombre}')

        for elemento in self.elementos:
            elemento.mostrar()

        print(f'Precio Total del Combo: {self.calcular_precio_total()}')

    def calcular_precio_total(self):
        return sum(elemento.precio for elemento in self.elementos)


class ComboDuo(ComponentMenu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.combo1 = None
        self.combo2 = None

    def personalizar(self, combo1, combo2):
        self.combo1 = combo1
        self.combo2 = combo2

    def mostrar(self):
        print(f'Combo Duo: {self.nombre}')
        if self.combo1:
            print(f'Menu:')
            self.combo1.mostrar()
        if self.combo2:
            print(f'Menu:')
            self.combo2.mostrar()
        print(f'Precio Total del Combo Duo: {self.calcular_precio_total()}')

    def calcular_precio_total(self):
        total_combo1 = self.combo1.calcular_precio_total() if self.combo1 else 0
        total_combo2 = self.combo2.calcular_precio_total() if self.combo2 else 0
        return total_combo1 + total_combo2

def solicitar_opcion(mensaje, opciones):
    while True:
        try:
            eleccion = int(input(mensaje))
            if eleccion in opciones:
                return eleccion
            else:
                print("Opción no válida. Por favor, elige una opción válida.")
        except ValueError:
            print("Error: Ingresa un número entero.")

if __name__ == "__main__":
     #Elementos individuales
    pizza_margarita = Pizza("Margarita", 10.0)
    pizza_pepperoni = Pizza("Pepperoni", 12.0)
    pizza_vegetariana = Pizza("Vegetariana", 11.0)
    pizza_hawaiana = Pizza("Hawaiana", 13.0)
    pizza_cuatros_quesos = Pizza("Cuatro Quesos", 14.0)

    bebida_cola = Bebida("Coca-Cola", 2.0)
    bebida_agua = Bebida("Agua", 1.5)
    bebida_fanta_de_naranja = Bebida("Fanta de Naranja", 2.0)
    bebida_cerveza = Bebida("Cerveza", 3.5)
    bebida_nestea=Bebida("Nestea", 2.0)

    entrante_ensalada = Entrante("Ensalada", 5.0)
    entrante_patatas = Entrante("Patatas", 4.0)
    entrante_alitas = Entrante("Alitas de Pollo", 6.0)
    entrante_nuggets = Entrante("Nuggets", 5.0)
    entrante_nachos = Entrante("Nachos", 5.0)

    postre_tarta_de_queso= Postre("Tarta de queso", 6.0)
    postre_helado = Postre("Helado", 3.0)
    postre_frutas = Postre("Frutas", 4.0)
    postre_natillas = Postre("Natillas", 3.0)
    postre_tarta_de_la_abuela = Postre("Tarta de la abuela", 5.0)


    # Combos predefinidos
    combo_1 = Combo("Combo 1")
    combo_1.agregar(entrante_ensalada)
    combo_1.agregar(pizza_margarita)
    combo_1.agregar(bebida_cola)
    combo_1.agregar(postre_helado)

    combo_2 = Combo("Combo 2")
    combo_2.agregar(entrante_patatas)
    combo_2.agregar(pizza_pepperoni)
    combo_2.agregar(bebida_agua)
    combo_2.agregar(postre_frutas)

    combo_3 = Combo("Combo 3")
    combo_3.agregar(entrante_alitas)
    combo_3.agregar(pizza_vegetariana)
    combo_3.agregar(bebida_fanta_de_naranja)
    combo_3.agregar(postre_natillas)

    combo_4 = Combo("Combo 4")
    combo_4.agregar(entrante_nuggets)
    combo_4.agregar(pizza_hawaiana)
    combo_4.agregar(bebida_cerveza)
    combo_4.agregar(postre_tarta_de_la_abuela)

  # Combo duo predefinidos

    combo_duo_1 = ComboDuo("Combo Duo 1")
    combo_duo_1.personalizar(combo_1, combo_2)

    combo_duo_2 = ComboDuo("Combo Duo2")
    combo_duo_2.personalizar(combo_3, combo_4)





    # Combos predefinidos
    print("\nCombos predefinidos:")
    combo_1.mostrar()
    combo_2.mostrar()
    combo_3.mostrar()
    combo_4.mostrar()
    print("\nCombos Duo predefinidos:")
    combo_pareja_1.mostrar()
    combo_pareja_2.mostrar()

    print("\nOpciones:")
    print("1. Crear combo personalizado")
    print("2. Elegir combo predefinido")
    print('3. Elegir combo Duo predefinido')
    print("4. Salir")
    eleccion = solicitar_opcion("Elige una opción (1, 2, 3 o 4): ", [1, 2, 3, 4])

    if eleccion == 1:
        # Solicitar al usuario que elija elementos para el combo personalizado
        print("\nElige los elementos para tu combo personalizado:")
        eleccion_entrante = solicitar_opcion(
            "\nOpciones de entrantes:\n1. Ensalada\n2. Patatas\n3. Alitas de Pollo\n4. Nuggets\n5. Nachos\nElige un entrante (1, 2, 3, 4 o 5): ",
            [1, 2, 3, 4, 5]
        )
        eleccion_pizza = solicitar_opcion(
            "\nOpciones de pizzas:\n1. Margarita\n2. Pepperoni\n3. Vegetariana\n4. Hawaiana\n5. Cuatro Quesos\nElige una pizza (1, 2, 3, 4 o 5): ",
            [1, 2, 3, 4, 5]
        )
        eleccion_bebida = solicitar_opcion(
            "\nOpciones de bebidas:\n1. Cola\n2. Agua\n3. Fanta de Naranja\n4. Cerveza\n5. Nestea\nElige una bebida (1, 2, 3, 4 o 5): ",
            [1, 2, 3, 4, 5]
        )
        eleccion_postre = solicitar_opcion(
            "\nOpciones de postres:\n1. Tarta de queso\n2. Helado\n3. Frutas\n4. Natillas\n5. Tarta de la abuela\nElige un postre (1, 2, 3, 4 o 5): ",
            [1, 2, 3, 4, 5]
        )

        # Crear el combo personalizado
        combo_personalizado = Combo("Combo Personalizado")
        # Agregar elementos al combo personalizado según las elecciones del usuario
        if eleccion_entrante == 1:
            combo_personalizado.agregar(entrante_ensalada)
        elif eleccion_entrante == 2:
            combo_personalizado.agregar(entrante_patatas)
        elif eleccion_entrante == 3:
            combo_personalizado.agregar(entrante_alitas)
        elif eleccion_entrante == 4:
            combo_personalizado.agregar(entrante_nuggets)
        elif eleccion_entrante == 5:
            combo_personalizado.agregar(entrante_nachos)

        if eleccion_pizza == 1:
            combo_personalizado.agregar(pizza_margarita)
        elif eleccion_pizza == 2:
            combo_personalizado.agregar(pizza_pepperoni)
        elif eleccion_pizza == 3:
            combo_personalizado.agregar(pizza_vegetariana)
        elif eleccion_pizza == 4:
            combo_personalizado.agregar(pizza_hawaiana)
        elif eleccion_pizza == 5:
            combo_personalizado.agregar(pizza_cuatros_quesos)

        if eleccion_bebida == 1:
            combo_personalizado.agregar(bebida_cola)
        elif eleccion_bebida == 2:
            combo_personalizado.agregar(bebida_agua)
        elif eleccion_bebida == 3:
            combo_personalizado.agregar(bebida_fanta_de_naranja)
        elif eleccion_bebida == 4:
            combo_personalizado.agregar(bebida_cerveza)
        elif eleccion_bebida == 5:
            combo_personalizado.agregar(bebida_nestea)

        if eleccion_postre == 1:
            combo_personalizado.agregar(postre_tarta_de_queso)
        elif eleccion_postre == 2:
            combo_personalizado.agregar(postre_helado)
        elif eleccion_postre == 3:
            combo_personalizado.agregar(postre_frutas)
        elif eleccion_postre == 4:
            combo_personalizado.agregar(postre_natillas)
        elif eleccion_postre == 5:
            combo_personalizado.agregar(postre_tarta_de_la_abuela)

        # Mostrar el combo personalizado
        print("\nTu combo personalizado:")
        combo_personalizado.mostrar()

    elif eleccion == 2:
        # Solicitar al usuario que elija un combo predefinido y mostrarlo
        opciones_combos_predefinidos = [1, 2, 3]
        eleccion_combo_predefinido = solicitar_opcion("Elige un combo predefinido (1, 2 o 3): ", opciones_combos_predefinidos)

        if eleccion_combo_predefinido == 1:
            combo_1.mostrar()
        elif eleccion_combo_predefinido == 2:
            combo_2.mostrar()
        elif eleccion_combo_predefinido == 3:
            combo_3.mostrar()

    elif eleccion == 3:
        combo_pareja_personalizado = ComboPareja("Combo Duo Personalizado")

        print("\nElige los combos para tu Combo Duo:")
        print("1. Combo 1")
        print("2. Combo 2")
        eleccion_combo1 = solicitar_opcion("Elige el Combo 1 (1 o 2): ", [1, 2])
        eleccion_combo2 = solicitar_opcion("Elige el Combo 2 (1 o 2): ", [1, 2])

        if eleccion_combo1 == 1:
            combo_duo_personalizado.personalizar(combo_1, None)
        elif eleccion_combo1 == 2:
            combo_duo_personalizado.personalizar(combo_2, None)

        if eleccion_combo2 == 1:
            combo_duo_personalizado.personalizar(combo_duo_personalizado.combo1, combo_1)
        elif eleccion_combo2 == 2:
            combo_duo_personalizado.personalizar(combo_duo_personalizado.combo1, combo_2)

        # Mostrar el Combo Duo personalizado
        print("\nTu Combo Pareja personalizado:")
        combo_pareja_personalizado.mostrar()

    elif eleccion == 4:
        print("\nGracias por usar nuestro servicio. Hasta pronto.")
        exit()


