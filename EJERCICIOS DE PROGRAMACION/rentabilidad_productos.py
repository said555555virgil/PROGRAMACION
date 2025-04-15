def ingresar_datos_productos(n):
    precios = []
    ventas = []
    
    for i in range(n):
        print(f"\nProducto {i+1}:")
        while True:
            try:
                precio = float(input("  Precio: "))
                if precio < 0:
                    print("  El precio no puede ser negativo.")
                    continue
                precios.append(precio)
                break
            except ValueError:
                print("  Entrada inválida. Intenta de nuevo.")
        
        while True:
            try:
                cantidad = int(input("  Cantidad vendida en la semana: "))
                if cantidad < 0:
                    print("  No puede ser negativo.")
                    continue
                ventas.append(cantidad)
                break
            except ValueError:
                print("  Entrada inválida. Intenta de nuevo.")
    
    return precios, ventas

def calcular_ingresos(precios, ventas):
    ingresos = [precios[i] * ventas[i] for i in range(len(precios))]
    return ingresos

def producto_mas_rentable(ingresos):
    max_ingreso = max(ingresos)
    producto = ingresos.index(max_ingreso) + 1
    return producto, max_ingreso

def main():
    num_productos = 60

    print("=== Rentabilidad Semanal de Productos ===")
    precios, ventas = ingresar_datos_productos(num_productos)

    ingresos = calcular_ingresos(precios, ventas)
    total_ingresos = sum(ingresos)
    ingreso_promedio = total_ingresos / num_productos
    producto_top, ingreso_top = producto_mas_rentable(ingresos)

    print("\n=== Resultados ===")
    for i in range(num_productos):
        print(f"Producto {i+1}: L. {ingresos[i]:.2f} de ingreso")

    print(f"\n💰 Total de ingresos: L. {total_ingresos:.2f}")
    print(f"📊 Ingreso promedio por producto: L. {ingreso_promedio:.2f}")
    print(f"🏆 Producto más rentable: Producto {producto_top} con L. {ingreso_top:.2f}")

if __name__ == "__main__":
    main()
