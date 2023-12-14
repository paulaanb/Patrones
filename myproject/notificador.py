# notificador.py

from observer import SujetoObservable

class Notificador(SujetoObservable):
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        if observador not in self.observadores:
            self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, evento):
        for observador in self.observadores:
            observador.actualizar(evento)
