from menu.models import Combo

class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get('carro')

        if not carro:
            carro={}
            carro = self.session['carro'] = {}
        #else:
        self.carro = carro

    def agregar(self, combo):
        if str(combo.id) not in self.carro.keys():
            self.carro[str(combo.id)] = {
                'combo_id': combo.id,
                'nombre': combo.nombre,
                'precio': str(combo.precio),
                'cantidad': 1,
                'imagen': combo.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(combo.id):
                    value['cantidad'] = value['cantidad'] + 1
                    value['precio'] = float(value['precio']) + combo.precio
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True

    def eliminar(self, combo):
        combo_id = str(combo.id) if isinstance(combo, Combo) else str(combo)
        if combo_id in self.carro:
            del self.carro[combo_id]
            self.guardar_carro()

    def restar_producto(self, combo):
        for key, value in self.carro.items():
            if key == str(combo.id):
                value['cantidad'] = value['cantidad'] - 1
                value['precio'] = float(value['precio']) - combo.precio
                if value['cantidad'] < 1:
                    self.eliminar(combo.id)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session['carro'] = {}
        self.session.modified = True
