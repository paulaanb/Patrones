# observer.py

from abc import ABC, abstractmethod

class SujetoObservable(ABC):
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, mensaje):
        for observador in self.observadores:
            observador.actualizar(mensaje)

class ComponentMenu(SujetoObservable, ABC):
    @abstractmethod
    def mostrar(self):
        pass

    @abstractmethod
    def obtener_precio(self, estrategia):
        pass
