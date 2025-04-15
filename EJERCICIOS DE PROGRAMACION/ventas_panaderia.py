def ingresar_ventas(num_panes, dias_semana):
    """
    Registra las ventas diarias por tipo de pan en una matriz.
    
    Retorna:
      List[List[int]]: Matriz con ventas por tipo de pan y día.
    """
    ventas = []
    for i in range(num_panes):
        print(f"\nTipo de pan {i+1}:")
        ventas_dia = []
        for j in range(dias_semana):
            while True:
                try:
                    cantidad = int(input(f"  Día {j+1}: "))
                    if cantidad < 0:
                        print("  La cantidad no puede ser negativa.")
                        continue
                    ventas_dia.append(cantidad)
                    break
                except ValueError:
                    print("  Entrada inválida. Intente nuevamente.")
        ventas.append(ventas_dia)
    return ventas

def calcular_totales(ventas):
    """
    Calcula el total semanal por tipo de pan.
    
    Retorna:
      List[int]: Totales por fila (tipo de pan).
    """
    totales = [sum(pan) for pan in ventas]
    return totales

def encontrar_mas_vendido(totales):
    """
    Identifica el tipo de pan más vendido.
    
    Retorna:
      Tuple[int, int]: (tipo de pan más vendido, total vendido)
    """
    max_venta = max(totales)
    tipo = totales.index(max_venta) + 1
    return tipo, max_venta

def main():
    num_panes = 10
    dias_semana = 7

    print("=== Registro de Ventas Semanales de Pan ===")
    ventas = ingresar_ventas(num_panes, dias_semana)
    
    totales = calcular_totales(ventas)
    
    tipo_mas_vendido, cantidad = encontrar_mas_vendido(totales)
    
    print("\n=== Resultados ===")
    for i, total in enumerate(totales):
        print(f"Tipo de pan {i+1}: {total} unidades vendidas en la semana.")
    
    print(f"\n➡️ El tipo de pan MÁS vendido fue el número {tipo_mas_vendido} con {cantidad} unidades.")

if __name__ == "__main__":
    main()

