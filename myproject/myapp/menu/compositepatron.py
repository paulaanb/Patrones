#compositepatron.py
from abc import ABC, abstractmethod
from myapp.menu.estrategias import EstrategiaPrecio
from myapp.menu.estrategias import EstrategiaPrecioNormal

class ComponentMenu(ABC):
    @abstractmethod
    def mostrar(self):
        pass

    def obtener_precio(self, estrategia):
        return estrategia.calcular_precio(self)

class Pizza(ComponentMenu):
    def __init__(self, nombre, precio, estrategia_precio=EstrategiaPrecioNormal()):
        self.nombre = nombre
        self.precio = precio
        self.estrategia_precio = estrategia_precio

    def mostrar(self):
        print(f'Pizza: {self.nombre} - Precio: {self.obtener_precio(self.estrategia_precio)}')

class Bebida(ComponentMenu):
    def __init__(self, nombre, precio, estrategia_precio=EstrategiaPrecioNormal()):
        self.nombre = nombre
        self.precio = precio
        self.estrategia_precio = estrategia_precio

    def mostrar(self):
        print(f'Bebida: {self.nombre} - Precio: {self.obtener_precio(self.estrategia_precio)}')

class Postre(ComponentMenu):
    def __init__(self, nombre, precio, estrategia_precio=EstrategiaPrecioNormal()):
        self.nombre = nombre
        self.precio = precio
        self.estrategia_precio = estrategia_precio

    def mostrar(self):
        print(f'Postre: {self.nombre} - Precio: {self.obtener_precio(self.estrategia_precio)}')

class Entrante(ComponentMenu):
    def __init__(self, nombre, precio, estrategia_precio=EstrategiaPrecioNormal()):
        self.nombre = nombre
        self.precio = precio
        self.estrategia_precio = estrategia_precio

    def mostrar(self):
        print(f'Entrante: {self.nombre} - Precio: {self.obtener_precio(self.estrategia_precio)}')

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

        print(f'Precio Total del Combo: {sum(elemento.obtener_precio(EstrategiaPrecioNormal()) for elemento in self.elementos)}')

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
        total_combo1 = self.combo1.obtener_precio(EstrategiaPrecioNormal()) if self.combo1 else 0
        total_combo2 = self.combo2.obtener_precio(EstrategiaPrecioNormal()) if self.combo2 else 0
        return total_combo1 + total_combo2
