from tabnanny import verbose
from django.db import models

from django.contrib.auth import get_user_mode
from django.db.models import F,Sum, FloatField 
from menu.models import Combo

User=get_user_model()


class Peticion(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)  

    @property
    def total(self):
        return self.lineapeticion_set.aggregate(

            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())

        )["total"] or FloatField(0)

    def __str__(self):
        return self.id


    class Meta:
        db_table='peticion'
        verbose_name='peticion'
        verbose_name_plural='peticiones'
        ordering=['id']


class LineaPeticion(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    combo=models.ForeignKey(Combo, on_delete=models.CASCADE)
    peticion=models.ForeignKey(Peticion, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} de {self.combo.nombre}'

    class Meta:
        db_table='lineapeticiones'
        verbose_name='Línea Peticion'
        verbose_name_plural='Líneas Peticiones'
        ordering=['id']

