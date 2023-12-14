def importe_total_carro(request):
    total = 0

    if request.user.is_authenticated:
        carro = request.session.get("carro", {})  

        for key, value in carro.items():
            total += float(value.get("precio", 0)) * int(value.get("cantidad", 0))

    else:
        total = 'Debe iniciar sesión'

    return {"importe_total_carro": total}
