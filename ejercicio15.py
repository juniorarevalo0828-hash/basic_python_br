import json

class Producto:

    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def calcular_total(self):
        return self.precio * self.cantidad

    def convertir_diccionario(self):
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "cantidad": self.cantidad,
            "total": self.calcular_total()
        }


productos = [
    Producto("Computador", 2500000, 2),
    Producto("Teclado", 150000, 5),
    Producto("Mouse", 80000, 3)
]

total_inventario = 0

for producto in productos:
    total_inventario += producto.calcular_total()


print("Valor total del inventario:", total_inventario)

productos_json = []

for producto in productos:
    productos_json.append(producto.convertir_diccionario())


with open("productos.json", "w", encoding="utf-8") as archivo:
    json.dump(
        productos_json,
        archivo,
        indent=4,
        ensure_ascii=False
    )

print("Información exportada correctamente a productos.json")
