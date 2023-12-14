# estrategias.py
from abc import ABC, abstractmethod

class EstrategiaPrecio(ABC):
    @abstractmethod
    def calcular_precio(self, producto):
        pass

class EstrategiaPrecioNormal(EstrategiaPrecio):
    def calcular_precio(self, producto):
        return producto.precio

class EstrategiaPrecioPromocional(EstrategiaPrecio):
    def calcular_precio(self, producto):
        # Lógica para calcular el precio con descuento/promoción
        return producto.precio * 0.9  #10% de descuento
