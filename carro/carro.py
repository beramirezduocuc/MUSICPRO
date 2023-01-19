class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carro = self.session.get("carro")
        if not self.carro:
            self.carro = self.session["carro"] = {}

    def agregar(self, producto):
        producto_id = str(producto.ID_producto)
        if(str(producto_id) not in self.carro.keys()):
            self.carro[producto_id] = {
            'producto_id': producto.ID_producto,
            'nombre': producto.Nombre,
            'precio': str(producto.Precio),
            'cantidad': 1,
            'imagen': producto.Imagen_Producto.url
        }
        else:
            for key,value in self.carro.items():
                if key==str(producto.ID_producto):
                    value["cantidad"]=value["cantidad"]+1
                break
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session['carro'] = self.carro
        self.session.modified = True
    
    def eliminar(self, producto):
        producto_id = str(producto.ID_producto)
        if producto_id in self.carro:
            del self.carro[producto_id]
            self.guardar_carro()


    def limpiar_carro(self):
        self.session['carro'] = {}
        self.session.modified = True
    
