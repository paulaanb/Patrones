# alianzas.py

class AlianzaEstrategica:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

class ProductoAlianza:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
