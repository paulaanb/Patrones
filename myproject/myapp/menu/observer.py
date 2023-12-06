from abc import ABC, abstractmethod

class Observador(ABC):
    @abstractmethod
    def actualizar(self, evento):
        pass

class Sujeto:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    def notificar_observadores(self, evento):
        for observador in self.observadores:
            observador.actualizar(evento)
class Notificador(Sujeto):
    def enviar_notificacion(self, evento):
        self.notificar_observadores(evento)
class ObservadorVinos(Observador):
    def actualizar(self, evento):
        # Lógica para manejar la notificación de nuevos vinos
        pass

class ObservadorCervezas(Observador):
    def actualizar(self, evento):
        # Lógica para manejar la notificación de promociones de cervezas
        pass
# Ejemplo de uso
notificador = Notificador()
cliente1 = ObservadorVinos()
cliente2 = ObservadorCervezas()

notificador.agregar_observador(cliente1)
notificador.agregar_observador(cliente2)

# Cuando haya un nuevo vino o una promoción de cerveza, se notifica a los observadores.
notificador.enviar_notificacion("Nuevo vino disponible")
notificador.enviar_notificacion("Promoción de cervezas")
