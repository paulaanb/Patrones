from django.contrib import admin
from .models import Peticion, LineaPeticion

# Register your models here.

admin.site.register([Peticion, LineaPeticion])
