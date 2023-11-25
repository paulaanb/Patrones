from abc import ABC, abstractmethod

class Component(ABC):
    @abstractmethod
    def tamaño(self):
        pass


class Documento(Component):
    def __init__(self, nombre, tipo, tamaño):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__tamaño = tamaño

    def tamaño(self):
        return self.__size

class Carpeta(Component):
    def __init__(self, nombre, elementos):
        self.__nombre = nombre
        self.__elementos = []

    def tamaño(self):
        total = 0
        for elemento in self.__elementos:
            total += elemento.tamaño()
        return total

    def agregar(self, elemento):
        self.__elementos.append(elemento)

    def eliminar(self, elemento):
        self.__elementos.remove(elemento)



class Enlace(Component):
    def __init__(self, nombre, destino):
        self.__nombre = nombre
        self.__url = destino

    def tamaño(self):
        return 0
    

    