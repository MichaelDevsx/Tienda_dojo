class Producto:
    def __init__(self,id,nombre,precio,categoria):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self,cambio_porcentaje,esta_elevado):
        if esta_elevado:
            self.precio = self.precio + ((self.precio * cambio_porcentaje) / 100)
        else:
            self.precio = self.precio - ((self.precio * cambio_porcentaje) / 100)

    def print_info(self):
        print(f'Producto = {self.nombre}, Precio = {self.precio}, Categoria = {self.categoria}')
