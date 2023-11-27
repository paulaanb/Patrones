from abc import ABC, abstractmethod
import csv
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
    

def guardar_elemento_csv(elemento, nombre_archivo, usuario):
    with open(nombre_archivo, 'a') as archivo:
        if isinstance(elemento, Combo):
            archivo.write(f'{usuario},Combo,{elemento.nombre},{elemento.calcular_precio_total()}\n')
            for subelemento in elemento.elementos:
                guardar_elemento_csv(subelemento, nombre_archivo, usuario)
        elif isinstance(elemento, ComboDuo):
            archivo.write(f'{usuario},ComboDuo,{elemento.nombre},{elemento.calcular_precio_total()}\n')
            if elemento.combo1:
                guardar_elemento_csv(elemento.combo1, nombre_archivo, usuario)
            if elemento.combo2:
                guardar_elemento_csv(elemento.combo2, nombre_archivo, usuario)
        elif isinstance(elemento, (Pizza, Bebida, Entrante, Postre)):
            archivo.write(f'{usuario},{type(elemento).__name__},{elemento.nombre},{elemento.precio}\n')

def guardar_elemento_csv(elemento, nombre_archivo, usuario):
    with open(nombre_archivo, 'a') as archivo:
        if isinstance(elemento, Combo):
            archivo.write(f'{usuario},Combo,{elemento.nombre},{elemento.calcular_precio_total()}\n')
            for subelemento in elemento.elementos:
                guardar_elemento_csv(subelemento, nombre_archivo, usuario)
        elif isinstance(elemento, ComboDuo):
            archivo.write(f'{usuario},ComboDuo,{elemento.nombre},{elemento.calcular_precio_total()}\n')
            if elemento.combo1:
                guardar_elemento_csv(elemento.combo1, nombre_archivo, usuario)
            if elemento.combo2:
                guardar_elemento_csv(elemento.combo2, nombre_archivo, usuario)
        elif isinstance(elemento, (Pizza, Bebida, Entrante, Postre)):
            archivo.write(f'{usuario},{type(elemento).__name__},{elemento.nombre},{elemento.precio}\n')

def leer_elementos_csv(nombre_archivo, usuario):
    elementos = []
    combos = {}

    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            usuario_archivo, tipo_elemento, nombre_elemento, precio_elemento = linea.strip().split(',')
            if usuario_archivo == usuario:
                if tipo_elemento == 'Combo':
                    combo = Combo(nombre_elemento)
                    combos[nombre_elemento] = combo
                    elementos.append(combo)
                elif tipo_elemento == 'ComboDuo':
                    combo_duo = ComboDuo(nombre_elemento)
                    combo_duo.combo1 = combos.get(nombre_elemento + "_1")
                    combo_duo.combo2 = combos.get(nombre_elemento + "_2")
                    elementos.append(combo_duo)
                elif tipo_elemento in ['Pizza', 'Bebida', 'Entrante', 'Postre']:
                    clase_elemento = globals()[tipo_elemento]
                    elemento = clase_elemento(nombre_elemento, float(precio_elemento))
                    elementos.append(elemento)

    return elementos




def preguntar_guardar_historial():
    while True:
        respuesta = input("¿Deseas guardar el historial de pedidos? (si/no): ").lower()
        if respuesta == 'si':
            return True
        elif respuesta == 'no':
            return False
        else:
            print("Respuesta no válida. Por favor, ingresa 'si' o 'no'.")


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
    # Solicitar al usuario que ingrese su nombre
    usuario = input("Introduce tu nombre de usuario: ")
    pedidos_usuario = leer_elementos_csv('pedidos.csv', usuario)

     # Crear instancias de elementos individuales (pizzas, bebidas, entrantes, postres)
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


    # Crear combos predefinidos
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

  # Crear combos Duo predefinidos

    combo_duo_1 = ComboDuo("Combo Duo 1")
    combo_duo_1.personalizar(combo_1, combo_2)

    combo_duo_2 = ComboDuo("Combo Duo 2")
    combo_duo_2.personalizar(combo_3, combo_4)





    # Mostrar combos predefinidos
    while True:
        print("\nCombos predefinidos:")
        combo_1.mostrar()
        combo_2.mostrar()
        combo_3.mostrar()
        combo_4.mostrar()
        print("\nCombos Duo predefinidos:")
        combo_duo_1.mostrar()
        combo_duo_2.mostrar()

        print("\nOpciones:")
        print("1. Crear combo personalizado")
        print("2. Elegir combo predefinido")
        print('3. Elegir combo Duo predefinido')
        print('4.Mostrar historial de pedidos')
        print("5. Salir")
        eleccion = solicitar_opcion("Elige una opción (1, 2, 3, 4 o 5): ", [1, 2, 3, 4, 5])

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
            #preguntamos si quiere guardar el historial
            if preguntar_guardar_historial():
                guardar_elemento_csv(combo_personalizado, 'pedidos.csv', usuario)
            else:
                print("No se guardará el historial de pedidos.")

        elif eleccion == 2:
            # Solicitar al usuario que elija un combo predefinido y mostrarlo
            opciones_combos_predefinidos = [1, 2, 3]
            eleccion_combo_predefinido = solicitar_opcion("Elige un combo predefinido (1, 2 o 3): ", opciones_combos_predefinidos)

            chosen_combo = None

            if eleccion_combo_predefinido == 1:
                chosen_combo = combo_1
            elif eleccion_combo_predefinido == 2:
                chosen_combo = combo_2
            elif eleccion_combo_predefinido == 3:
                chosen_combo = combo_3

            # Mostrar el combo predefinido
            print("\nEl combo predefinido que has elegido es:")
            chosen_combo.mostrar()

            # Preguntar si quieren pedir este combo
            if input("¿Quieres pedir este combo? (si/no): ").lower() == 'si':
                if preguntar_guardar_historial():
                    guardar_elemento_csv(chosen_combo, 'pedidos.csv', usuario)
                else:
                    print("No se guardará el historial de pedidos.")
            else:
                print("Pedido cancelado.")

        elif eleccion == 3:
            combo_duo_personalizado = ComboDuo("Combo Duo Personalizado")

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
            print("\nTu Combo Duo personalizado:")
            combo_duo_personalizado.mostrar()
            #preguntamos si quiere guardar el historial
            if preguntar_guardar_historial():
                guardar_elemento_csv(combo_duo_personalizado, 'pedidos.csv', usuario)
            else:
                print("No se guardará el historial de pedidos.")

        elif eleccion == 4:
    # Mostrar historial de pedidos según usuario
            print("\nHistorial de pedidos:")
            pedidos_usuario = leer_elementos_csv('pedidos.csv', usuario)

            if pedidos_usuario:
                print(f"\nPedidos antiguos de {usuario}:")
                for pedido in pedidos_usuario:
                    if isinstance(pedido, Combo):
                        print("\nPedido Combo:")
                        pedido.mostrar()
                    elif isinstance(pedido, ComboDuo):
                        print("\nPedido Combo Duo:")
                        pedido.mostrar()
                    else:
                        print(f'{type(pedido).__name__}: {pedido.nombre} - Precio: {pedido.precio}')
            else:
                print(f"No hay pedidos antiguos de {usuario}.")


        elif eleccion == 5:
            # Salir del programa
            print("Saliendo del programa...")
            break

    