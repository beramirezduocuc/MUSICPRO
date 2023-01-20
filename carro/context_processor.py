from .carro import Carro
def importe_total_carro(request):
    carro = Carro(request)
    total = 0
    for key,value in carro.carro.items():
        total = total +(float(value["precio"])*value["cantidad"])
    return {"importe_total_carro":total}

def subtotal(request):
    carro = Carro(request)
    total = 0
    for key,value in carro.carro.items():
        total = total +(float(value["precio"])*value["cantidad"])
    return {"importe_total_carro":total}
