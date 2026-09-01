class Producto:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_total(self):
        return self.precio * self.cantidad


producto = Producto("Computador", 2500000, 2)

total = producto.calcular_total()

print("Producto:", producto.nombre)
print("Valor total del inventario:", total)
