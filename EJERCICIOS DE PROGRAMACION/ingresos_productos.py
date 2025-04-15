def ingresar_datos_productos(num_productos):
    """
    Permite ingresar el precio y unidades vendidas de cada producto.
    
    Retorna:
      precios (List[float]): Lista con precios de cada producto.
      cantidades (List[int]): Lista con cantidades vendidas de cada producto.
    """
    precios = []
    cantidades = []
    for i in range(num_productos):
        print(f"\nProducto {i+1}:")
        while True:
            try:
                precio = float(input("  Precio: "))
                if precio < 0:
                    print("  El precio debe ser mayor o igual a 0.")
                    continue
                cantidad = int(input("  Unidades vendidas: "))
                if cantidad < 0:
                    print("  La cantidad debe ser mayor o igual a 0.")
                    continue
                precios.append(precio)
                cantidades.append(cantidad)
                break
            except ValueError:
                print("  Entrada inválida. Intente nuevamente.")
    return precios, cantidades

def calcular_ingresos(precios, cantidades):
    """
    Calcula los ingresos por producto.
    
    Retorna:
      List[float]: Lista de ingresos por cada producto.
    """
    ingresos = [precios[i] * cantidades[i] for i in range(len(precios))]
    return ingresos

def producto_mayor_menor_ingreso(ingresos):
    """
    Identifica los productos con más y menos ingresos.
    
    Retorna:
      Tuple[int, float], Tuple[int, float]: (índice, ingreso mayor), (índice, ingreso menor)
    """
    max_ingreso = max(ingresos)
    min_ingreso = min(ingresos)
    prod_max = ingresos.index(max_ingreso) + 1
    prod_min = ingresos.index(min_ingreso) + 1
    return (prod_max, max_ingreso), (prod_min, min_ingreso)

def main():
    num_productos = 50
    print("=== Ingresos por Producto en Tienda ===")

    # Ingresar datos
    precios, cantidades = ingresar_datos_productos(num_productos)

    # Calcular ingresos
    ingresos = calcular_ingresos(precios, cantidades)

    # Identificar productos con más y menos ingresos
    (prod_max, max_ing), (prod_min, min_ing) = producto_mayor_menor_ingreso(ingresos)

    # Mostrar resultados
    print("\n=== Resultados ===")
    for i in range(num_productos):
        print(f"Producto {i+1}: Ingreso = L {ingresos[i]:.2f}")
    print(f"\nProducto con MÁS ingreso: Producto {prod_max} (L {max_ing:.2f})")
    print(f"Producto con MENOS ingreso: Producto {prod_min} (L {min_ing:.2f})")

if __name__ == "__main__":
    main()
