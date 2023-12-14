from django import forms

class PizzaBuilderForm(forms.Form):
    masa=forms.ChoiceField(choices=[('fina','Fina'),('gruesa','Gruesa')])
    salsa=forms.ChoiceField(choices=[('tomate','Tomate'),('carbonara','Carbonara')])
    ingredientes_principales=forms.MultipleChoiceField(choices=[
            ('tomate', 'Tomate'), ('queso', 'Queso'), ('jamon', 'Jamón'),
            ('atun', 'Atún'), ('champiñones', 'Champiñones'), ('bacon', 'Bacon'),
            ('cebolla', 'Cebolla'), ('pollo', 'Pollo'), ('piña', 'Piña'),
            ('aceitunas', 'Aceitunas'), ('anchoas', 'Anchoas'), ('maiz', 'Maíz'),
            ('salchichas', 'Salchichas'), ('pimiento', 'Pimiento'), ('gambas', 'Gambas'),
            ('carne_picada', 'Carne Picada'), ('huevo', 'Huevo')
        ], 
        widget=forms.CheckboxSelectMultiple)
    coccion=forms.ChoiceField(choices=[('horno','Horno'),('piedra','Piedra')])
    presentacion=forms.ChoiceField(choices=[('entera', 'Entera'), ('porciones', 'En Porciones')])
    maridaje_recomendado=forms.ChoiceField(
        choices=[
            ('cerveza', 'Cerveza'), ('vino_blanco', 'Vino Blanco'), ('vino_tinto', 'Vino Tinto'),
            ('sangria', 'Sangría'), ('cocacola', 'Coca-Cola'), ('fanta_naranja', 'Fanta Naranja'),
            ('fanta_limon', 'Fanta Limón'), ('agua', 'Agua')
        ]
    )
    extra_bordes_queso = forms.ChoiceField(choices=[('si', 'Sí'), ('no', 'No')], widget=forms.RadioSelect)

    