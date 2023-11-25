# myapp/models.py
from django.db import models

class MenuItem(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(MenuItem)
    is_combo = models.BooleanField(default=False)
    discount = models.FloatField(default=0.0)

    def __str__(self):
        return self.name
