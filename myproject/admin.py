from django.contrib import admin
from .models import CategoriaProd, Componente, Combo

class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class ComponenteAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
class ComboAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Componente, ComponenteAdmin)
admin.site.register(Combo, ComboAdmin)



