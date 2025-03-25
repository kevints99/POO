Descripción
Este programa define una clase `Producto` que representa un producto en una tienda, con atributos como nombre, precio y stock. También incluye métodos para verificar disponibilidad, vender y reabastecer el producto.

Estructura del Código
El código contiene lo siguiente:
  - Clase `Producto`:
  - `__init__(self, nombre, precio, stock)`: Constructor que inicializa los atributos del producto.
  - `verificar_disponibilidad(self, cantidad)`: Método que verifica si hay suficiente stock para vender una cantidad solicitada.
  - `vender(self, cantidad)`: Método que reduce el stock si hay disponibilidad o muestra un mensaje de falta de stock.
  - `reabastecer(self, cantidad)`: Método que aumenta el stock del producto.

Ejemplo de uso:
  - Se crea un producto "Laptop" con un precio de 1200 y un stock inicial de 10 unidades.
  - Se verifica la disponibilidad de 5 unidades.
  - Se venden 3 unidades.
  - Se verifica si hay 8 unidades disponibles.
  - Se intenta vender 8 unidades (debe fallar por falta de stock).
  - Se reabastece con 10 unidades adicionales.
  - Se verifica nuevamente la disponibilidad de 8 unidades.
  - Se venden 8 unidades.
