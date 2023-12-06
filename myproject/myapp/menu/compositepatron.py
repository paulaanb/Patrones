from abc import ABC, abstractmethod
from myapp.menu.estrategias import EstrategiaPrecio, EstrategiaPrecioNormal
from myapp.menu.observer import SujetoObservable

class ComponentMenu(SujetoObservable, ABC):
    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def obtener_precio(self, estrategia):
        pass

    @abstractmethod
    def introducir_nuevo_producto(self, nombre):
        pass
class Pizza(ComponentMenu):
    def __init__(self, nombre, precio, estrategia_precio=EstrategiaPrecioNormal()):
        self.nombre = nombre
        self.precio = precio
        self.estrategia_precio = estrategia_precio

    def mostrar(self):
        print(f'Pizza: {self.nombre} - Precio: {self.obtener_precio(self.estrategia_precio)}')
        
    def introducir_nuevo_producto(self, nombre):
        mensaje = f"Nuevo producto introducido: {nombre}"
        self.notificar_observadores(mensaje)
class Bebida(ComponentMenu):
    def __init__(self, nombre, precio, estrategia_precio=EstrategiaPrecioNormal()):
        self.nombre = nombre
        self.precio = precio
        self.estrategia_precio = estrategia_precio

    def mostrar(self):
        print(f'Bebida: {self.nombre} - Precio: {self.obtener_precio(self.estrategia_precio)}')
        
    def introducir_nuevo_producto(self, nombre):
        mensaje = f"Nuevo producto introducido: {nombre}"
        self.notificar_observadores(mensaje)
class Postre(ComponentMenu):
    def __init__(self, nombre, precio, estrategia_precio=EstrategiaPrecioNormal()):
        self.nombre = nombre
        self.precio = precio
        self.estrategia_precio = estrategia_precio

    def mostrar(self):
        print(f'Postre: {self.nombre} - Precio: {self.obtener_precio(self.estrategia_precio)}')

    def introducir_nuevo_producto(self, nombre):
        mensaje = f"Nuevo producto introducido: {nombre}"
        self.notificar_observadores(mensaje)       

class Entrante(ComponentMenu):
    def __init__(self, nombre, precio, estrategia_precio=EstrategiaPrecioNormal()):
        self.nombre = nombre
        self.precio = precio
        self.estrategia_precio = estrategia_precio

    def mostrar(self):
        print(f'Entrante: {self.nombre} - Precio: {self.obtener_precio(self.estrategia_precio)}')

    def introducir_nuevo_producto(self, nombre):
        mensaje = f"Nuevo producto introducido: {nombre}"
        self.notificar_observadores(mensaje)
class Combo(ComponentMenu):
    def __init__(self, nombre):
        self.nombre = nombre
        self.elementos = []

    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self, elemento):
        self.elementos.remove(elemento)
        
    def introducir_nuevo_producto(self, nombre):
        mensaje = f"Nuevo producto introducido: {nombre}"
        self.notificar_observadores(mensaje)        
    
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
    
    def introducir_nuevo_producto(self, nombre):
        mensaje = f"Nuevo producto introducido: {nombre}"
        self.notificar_observadores(mensaje)

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
class EstrategiaPrecio(ABC):
    @abstractmethod
    def aplicar_descuento(self, precio):
        pass

class EstrategiaPrecioDescuento(EstrategiaPrecio):
    def __init__(self, porcentaje_descuento):
        self.porcentaje_descuento = porcentaje_descuento

    def aplicar_descuento(self, precio):
        descuento = precio * (self.porcentaje_descuento / 100)
        return precio - descuento

class EstrategiaPrecioPromocion(EstrategiaPrecio):
    def __init__(self, monto_promocion):
        self.monto_promocion = monto_promocion

    def aplicar_descuento(self, precio):
        return max(precio - self.monto_promocion, 0)

class ClienteSuscriptor(SujetoObservable):
    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def actualizar(self, mensaje):
        if self.categoria.lower() in mensaje.lower():
            print(f"Cliente {self.nombre}: {mensaje}")