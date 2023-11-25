from django.db import models
from django.dispatch import receiver
from django.db.models.signals import m2m_changed 

class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoriaProd"
        verbose_name_plural = "categoriasProd"

    def __str__(self):
        return self.nombre

class Componente(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='menu', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "componente"
        verbose_name_plural = "componentes"

    def mostrar(self):
        print(f'{self.categoria}: {self.nombre} - Precio: {self.precio}')

class Combo(models.Model):
    nombre = models.CharField(max_length=50)
    componentes = models.ManyToManyField(Componente)
    created = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='menu', null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    precio = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = "combo"
        verbose_name_plural = "combos"

    def mostrar(self):
        print(f'Combo: {self.nombre}')
        for componente in self.componentes.all():
            componente.mostrar()
        print(f'Precio Total del Combo: {self.calcular_precio_total()}')

    def calcular_precio_total(self):
        return sum(componente.precio for componente in self.componentes.all())
    

