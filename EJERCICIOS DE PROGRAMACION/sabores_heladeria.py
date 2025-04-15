def ingresar_ventas(num_sabores):
    ventas = []
    for i in range(num_sabores):
        while True:
            try:
                cantidad = int(input(f"Ventas del sabor {i+1}: "))
                if cantidad < 0:
                    print("  No puede ser negativo.")
                    continue
                ventas.append(cantidad)
                break
            except ValueError:
                print("  Entrada inválida. Intenta nuevamente.")
    return ventas

def encontrar_mas_y_menos_vendido(ventas):
    max_ventas = max(ventas)
    min_ventas = min(ventas)
    
    sabor_mas = ventas.index(max_ventas) + 1
    sabor_menos = ventas.index(min_ventas) + 1
    
    return sabor_mas, max_ventas, sabor_menos, min_ventas

def main():
    num_sabores = 30
    print("=== Registro de Ventas de Sabores de Helado ===")

    ventas = ingresar_ventas(num_sabores)

    sabor_mas, cant_mas, sabor_menos, cant_menos = encontrar_mas_y_menos_vendido(ventas)

    print("\n=== Resultados ===")
    for i, cantidad in enumerate(ventas):
        print(f"Sabor {i+1}: {cantidad} ventas")

    print(f"\n🍨 Sabor MÁS vendido: Sabor {sabor_mas} con {cant_mas} ventas")
    print(f"🥶 Sabor MENOS vendido: Sabor {sabor_menos} con {cant_menos} ventas")

if __name__ == "__main__":
    main()
