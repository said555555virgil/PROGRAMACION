def ingresar_pedidos(num_platos, dias=7):
    pedidos = []
    for i in range(num_platos):
        total_pedidos = 0
        for dia in range(dias):
            while True:
                try:
                    cantidad = int(input(f"¿Cuántas veces se pidió el plato {i+1} en el día {dia+1}? "))
                    if cantidad < 0:
                        print("  No puede ser negativo.")
                        continue
                    total_pedidos += cantidad
                    break
                except ValueError:
                    print("  Entrada inválida. Intenta nuevamente.")
        pedidos.append(total_pedidos)
    return pedidos

def plato_mas_pedido(pedidos):
    max_pedido = max(pedidos)
    plato_max = pedidos.index(max_pedido) + 1
    return plato_max, max_pedido

def main():
    num_platos = 60
    print("=== Registro de Platos Más Pedidos en Restaurante ===")
    
    pedidos = ingresar_pedidos(num_platos)
    plato_max, max_pedido = plato_mas_pedido(pedidos)
    
    print("\n=== Resultados ===")
    print(f"🍽️ El plato MÁS pedido de la semana fue el plato {plato_max} con {max_pedido} pedidos")

if __name__ == "__main__":
    main()
