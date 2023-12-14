from component import Component
class Archivo(Component):
     def __init__(self, nombre, tipo, tamano):
         self.nombre = nombre
         self.tipo = tipo
         self.tamano = tamano

     def tamaño(self):
         return self.tamano

 