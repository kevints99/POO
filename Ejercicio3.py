class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def verificar_disponibilidad(self, cantidad):
        return self.stock >= cantidad
    
    def vender(self, cantidad):
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"Se han vendido {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}.")
        else:
            print(f"No hay suficiente stock de {self.nombre} para vender {cantidad} unidades.")
    
    def reabastecer(self, cantidad):
        self.stock += cantidad
        print(f"Se han agregado {cantidad} unidades de {self.nombre}. Stock actual: {self.stock}.")

# Ejemplo de uso
producto = Producto("Laptop", 1200, 10)
print(producto.verificar_disponibilidad(5))  # Verifica si hay 5 unidades disponibles
producto.vender(3)  # Vender 3 unidades
print(producto.verificar_disponibilidad(8))  # Verifica si hay 8 unidades disponibles
producto.vender(8)  # Intentar vender 8 unidades (debe fallar)
producto.reabastecer(10)  # Reabastecer con 10 unidades adicionales
print(producto.verificar_disponibilidad(8))  # Verificar nuevamente si hay 8 unidades disponibles
producto.vender(8)  # Vender 8 unidades
