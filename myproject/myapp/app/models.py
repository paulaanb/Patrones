from django.db import models
from abc import ABC, abstractmethod


class PizzaBuilder(ABC):

    @abstractmethod
    def añadir_masa(self):
        pass

    @abstractmethod
    def añadir_salsa(self):
        pass

    @abstractmethod
    def añadir_ingredientes_principales(self):
        pass

    @abstractmethod
    def añadir_coccion(self):
        pass

    @abstractmethod
    def añadir_presentacion(self):
        pass

    @abstractmethod
    def añadir_maridaje_recomendado(self):
        pass

    @abstractmethod
    def añadir_extra(self):
        pass


class Pizza(models.Model):
    masa = models.CharField(max_length=255)
    salsa = models.CharField(max_length=255)
    ingredientes_principales = models.CharField(max_length=255)
    coccion = models.CharField(max_length=255)
    presentacion = models.CharField(max_length=255)
    maridaje_recomendado = models.CharField(max_length=255)
    extra = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.masa} Pizza"