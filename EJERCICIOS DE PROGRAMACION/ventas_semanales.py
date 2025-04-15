def ingresar_ventas(num_productos, num_dias):
    """
    Registra las ventas diarias para cada producto en una matriz.
    
    Retorna:
      List[List[int]]: Matriz con ventas por producto y día.
    """
    ventas = []
    for i in range(num_productos):
        print(f"\nProducto {i+1}:")
        fila = []
        for j in range(num_dias):
            while True:
                try:
                    cantidad = int(input(f"  Día {j+1}: "))
                    if cantidad < 0:
                        print("  La cantidad no puede ser negativa.")
                        continue
                    fila.append(cantidad)
                    break
                except ValueError:
                    print("  Entrada inválida. Intente nuevamente.")
        ventas.append(fila)
    return ventas

def calcular_totales_productos(ventas):
    """
    Suma las ventas semanales por producto.
    
    Retorna:
      List[int]: Totales de ventas por producto.
    """
    return [sum(producto) for producto in ventas]

def encontrar_mas_vendido(totales):
    """
    Encuentra el producto más vendido.
    
    Retorna:
      Tuple[int, int]: (producto más vendido, unidades vendidas)
    """
    max_ventas = max(totales)
    producto = totales.index(max_ventas) + 1
    return producto, max_ventas

def main():
    num_productos = 20
    num_dias = 7
    
    print("=== Registro de Ventas Semanales ===")
    ventas = ingresar_ventas(num_productos, num_dias)
    
    totales = calcular_totales_productos(ventas)
    
    producto_mas_vendido, cantidad = encontrar_mas_vendido(totales)
    
    print("\n=== Resultados ===")
    for i, total in enumerate(totales):
        print(f"Producto {i+1}: {total} unidades vendidas en la semana.")
    
    print(f"\n🏆 Producto MÁS vendido: Producto {producto_mas_vendido} con {cantidad} unidades.")

if __name__ == "__main__":
    main()
