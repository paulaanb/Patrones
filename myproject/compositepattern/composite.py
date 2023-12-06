from abc import ABC, abstractmethod
import csv
from myapp.menu.compositepatron import Pizza, Bebida, Postre, Entrante, Combo, ComboDuo
from myapp.menu.estrategias import EstrategiaPrecioNormal, EstrategiaPrecioPromocional
from myapp.menu.observer import SujetoObservable, ComponentMenu
from myapp.menu.alianza import AlianzaEstrategica, ProductoAlianza

# Clases del Composite Pattern
class ComponentMenu(ABC):
    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def calcular_precio_total(self):
        pass


class Pizza(ComponentMenu):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f'Pizza: {self.nombre} - Precio: {self.precio}')

    def calcular_precio_total(self):
        return self.precio


class Bebida(ComponentMenu):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f'Bebida: {self.nombre} - Precio: {self.precio}')

    def calcular_precio_total(self):
        return self.precio


class Postre(ComponentMenu):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f'Postre: {self.nombre} - Precio: {self.precio}')

    def calcular_precio_total(self):
        return self.precio


class Entrante(ComponentMenu):
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar(self):
        print(f'Entrante: {self.nombre} - Precio: {self.precio}')

    def calcular_precio_total(self):
        return self.precio


class Combo(ComponentMenu):
    def __init__(self, nombre, estrategia_precio=None):
        self.nombre = nombre
        self.elementos = []
        self.estrategia_precio = estrategia_precio

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self, elemento):
        self.elementos.remove(elemento)

    def mostrar(self):
        print(f'Combo: {self.nombre}')

        for elemento in self.elementos:
            elemento.mostrar()

        precio_total = self.calcular_precio_total()
        if self.estrategia_precio:
            precio_total = self.estrategia_precio.aplicar_descuento(precio_total)

        print(f'Precio Total del Combo: {precio_total}')

    def calcular_precio_total(self):
        return sum(elemento.calcular_precio_total() for elemento in self.elementos)


class ComboDuo(ComponentMenu):
    def __init__(self, nombre, estrategia_precio=None):
        self.nombre = nombre
        self.combo1 = None
        self.combo2 = None
        self.estrategia_precio = estrategia_precio

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

        precio_total = self.calcular_precio_total()
        if self.estrategia_precio:
            precio_total = self.estrategia_precio.aplicar_descuento(precio_total)

        print(f'Precio Total del Combo Duo: {precio_total}')

    def calcular_precio_total(self):
        total_combo1 = self.combo1.calcular_precio_total() if self.combo1 else 0
        total_combo2 = self.combo2.calcular_precio_total() if self.combo2 else 0
        return total_combo1 + total_combo2


# Estrategias para el patrón Strategy
class EstrategiaPrecioDescuento:
    def __init__(self, descuento_porcentaje):
        self.descuento_porcentaje = descuento_porcentaje

    def aplicar_descuento(self, precio):
        return precio - (precio * self.descuento_porcentaje / 100)


class EstrategiaPrecioPromocion:
    def __init__(self, promocion_precio):
        self.promocion_precio = promocion_precio

    def aplicar_descuento(self, precio):
        return self.promocion_precio


class EstrategiaPrecioNormal:
    def aplicar_descuento(self, precio):
        return precio

# Funciones para guardar y leer elementos desde un archivo CSV
def guardar_elemento_csv(elemento, nombre_archivo, usuario):
    with open(nombre_archivo, 'a') as archivo:
        if isinstance(elemento, Combo):
            archivo.write(f'{usuario},Combo,{elemento.nombre},{elemento.calcular_precio_total()}\n')
        elif isinstance(elemento, ComboDuo):
            archivo.write(f'{usuario},ComboDuo,{elemento.nombre},{elemento.calcular_precio_total()}\n')
        else:
            archivo.write(f'{usuario},{elemento.__class__.__name__},{elemento.nombre},{elemento.precio}\n')


def leer_elementos_csv(nombre_archivo):
    elementos = []

    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        for linea in lector_csv:
            usuario = linea[0]
            tipo_elemento = linea[1]
            nombre_elemento = linea[2]
            precio_elemento = float(linea[3])

            if tipo_elemento == 'Pizza':
                elemento = Pizza(nombre_elemento, precio_elemento)
            elif tipo_elemento == 'Bebida':
                elemento = Bebida(nombre_elemento, precio_elemento)
            elif tipo_elemento == 'Postre':
                elemento = Postre(nombre_elemento, precio_elemento)
            elif tipo_elemento == 'Entrante':
                elemento = Entrante(nombre_elemento, precio_elemento)
            elif tipo_elemento == 'Combo':
                elemento = Combo(nombre_elemento)
            elif tipo_elemento == 'ComboDuo':
                elemento = ComboDuo(nombre_elemento)

            elementos.append(elemento)

    return elementos

def solicitar_opcion(mensaje, opciones_validas):
    while True:
        try:
            eleccion = int(input(mensaje))
            if eleccion in opciones_validas:
                return eleccion
            else:
                print("Opción no válida. Introduce un valor válido.")
        except ValueError:
            print("Por favor, introduce un número válido.")
def preguntar_guardar_historial():
    while True:
        respuesta = input("¿Quieres guardar el historial de pedidos? (si/no): ").lower()
        if respuesta in ['si', 'no']:
            return respuesta == 'si'
        else:
            print("Por favor, responde con 'si' o 'no'.")

class ClienteSuscriptor(SujetoObservable):
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def actualizar(self, mensaje):
        if self.categoria.lower() in mensaje.lower():
            print(f"Cliente {self.nombre}: {mensaje}")
def main():
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

    # Estrategias de precio
    estrategia_descuento_10 = EstrategiaPrecioDescuento(10)
    estrategia_promocion_25 = EstrategiaPrecioPromocion(25)

    # Asignar estrategias a combos específicos
    combo_1.estrategia_precio = estrategia_descuento_10
    combo_3.estrategia_precio = estrategia_promocion_25
    
    # Crear instancias de productos o promociones
    pizza_especial = Pizza("Pizza Especial", 15.0)
    cerveza_promocion = Bebida("Cerveza Promocional", 3.0)
    postre_del_dia = Postre("Postre del Día", 5.0)

    # Introducir nuevos productos y notificar a los suscriptores
    pizza_especial.introducir_nuevo_producto("Pizza Especial del Chef")
    cerveza_promocion.introducir_nuevo_producto("¡Nueva Cerveza en Promoción!")
    postre_del_dia.introducir_nuevo_producto("Descubre nuestro Postre Especial")

    # Crear instancias de clientes suscriptores
    cliente_vinos = ClienteSuscriptor("Amante de Vinos", "Pizza")
    cliente_cervezas = ClienteSuscriptor("Fanático de Cervezas", "Bebida")
    cliente_postres = ClienteSuscriptor("Dulce Amante", "Postre")

    # Suscribir a los clientes a las categorías de su interés
    pizza_especial.agregar_observador(cliente_vinos)
    cerveza_promocion.agregar_observador(cliente_cervezas)
    postre_del_dia.agregar_observador(cliente_postres)

    # Crear una alianza estratégica
    alianza_vinos = AlianzaEstrategica("Alianza de Vinos", "Explora nuestra selección exclusiva de vinos")

    # Crear productos de aliados estratégicos
    vino_tinto = ProductoAlianza("Vino Tinto Especial", 25.0, "Vino tinto de la región vinícola reconocida")
    vino_blanco = ProductoAlianza("Vino Blanco Selecto", 20.0, "Refrescante vino blanco de la mejor calidad")

    # Agregar productos de aliados estratégicos a la alianza
    alianza_vinos.agregar_producto(vino_tinto)
    alianza_vinos.agregar_producto(vino_blanco)

    # Agregar alianza estratégica a tu sistema
    pizza_margarita.agregar_alianza_estrategica(alianza_vinos)

    # Actualizar productos de aliados estratégicos
    vino_tinto.precio = 30.0
    vino_tinto.descripcion = "Vino tinto de edición limitada, añada 2020"

    # Mostrar productos actualizados
    print(f"Precio actualizado del {vino_tinto.nombre}: {vino_tinto.precio}")
    print(f"Descripción actualizada del {vino_tinto.nombre}: {vino_tinto.descripcion}")
    
    # Solicitar al usuario que ingrese su nombre
    usuario = input("Introduce tu nombre de usuario: ")

    try:
        # Intentar leer el archivo de pedidos existente
        pedidos_usuario = leer_elementos_csv('pedidos.csv')
    except FileNotFoundError:
        # Si no existe, crear un nuevo archivo
        print("El archivo 'pedidos.csv' no se encuentra en el directorio especificado. Se creará un nuevo archivo.")
        with open('pedidos.csv', 'w') as nuevo_archivo:
            nuevo_archivo.write("Usuario,Tipo,Elemento,Precio\n")
        # Intentar leer el archivo nuevamente
        pedidos_usuario = leer_elementos_csv('pedidos.csv')

    # Mostrar combos predefinidos y opciones
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
        print('4. Mostrar historial de pedidos')
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

    