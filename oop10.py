

class Tienda:
    def __init__(self,nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self,producto):
        self.productos.append(producto)
        print('Producto agregado')

    def vender_producto(self,id):
        for i,producto in enumerate(self.productos):
            if producto.id == id:
                self.productos.pop(i)

    def ver_productos(self):
        for producto in self.productos:
            producto.print_info()

    def inflacion(self,porcentaje_aumento):
        for producto in self.productos:
            producto.actualizar_precio(porcentaje_aumento,True)

    def hacer_liquidacion(self,porcentaje_descuento,categoria):
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.actualizar_precio(porcentaje_descuento,False)


