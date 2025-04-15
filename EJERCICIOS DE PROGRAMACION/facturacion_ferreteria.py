def ingresar_ventas():
    """
    Permite al usuario ingresar los datos de cada venta: código de artículo y cantidad vendida.
    El ingreso finaliza cuando se escribe 'fin' en el código.
    
    Retorna:
      List[Tuple[int, int]]: Lista con los pares (código, cantidad)
    """
    ventas = []
    print("Ingrese los datos de cada artículo vendido (escriba 'fin' para terminar):")
    while True:
        codigo_input = input("Código del artículo: ")
        if codigo_input.lower() == "fin":
            break
        try:
            codigo = int(codigo_input)
            cantidad = int(input("Cantidad vendida: "))
        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
            continue
        ventas.append((codigo, cantidad))
    return ventas

def calcular_total_por_articulo(ventas, precios):
    """
    Calcula el precio total por artículo usando el código y la cantidad.
    
    Parámetros:
      ventas (List[Tuple[int, int]]): Lista de ventas con (código, cantidad).
      precios (Dict[int, float]): Diccionario que asocia cada código con su precio unitario.
      
    Retorna:
      List[Tuple[int, int, float, float]]: Lista de detalles con (código, cantidad, precio_unitario, total)
    """
    detalles = []
    for codigo, cantidad in ventas:
        if codigo in precios:
            precio_unitario = precios[codigo]
            total_articulo = cantidad * precio_unitario
            detalles.append((codigo, cantidad, precio_unitario, total_articulo))
        else:
            print(f"El código {codigo} no existe en el catálogo de precios.")
    return detalles

def calcular_subtotal(detalles):
    """
    Calcula el subtotal sumando el total de cada artículo vendido.
    
    Parámetros:
      detalles (List[Tuple[int, int, float, float]]): Lista de detalles por artículo.
      
    Retorna:
      float: Subtotal de la factura.
    """
    return sum(total for _, _, _, total in detalles)

def calcular_total_general(subtotal, tasa_isv=0.15):
    """
    Calcula el impuesto (ISV) y el total general de la factura.
    
    Parámetros:
      subtotal (float): Subtotal de la factura.
      tasa_isv (float): Tasa de impuesto (por defecto 15%).
      
    Retorna:
      Tuple[float, float]: ISV calculado y total general (subtotal + ISV)
    """
    isv = subtotal * tasa_isv
    total_general = subtotal + isv
    return isv, total_general

def mostrar_factura(detalles, subtotal, isv, total_general):
    """
    Muestra en pantalla el detalle de la factura.
    """
    print("\nDetalle de la Factura:")
    print("-" * 50)
    print(f"{'Código':<10}{'Cantidad':<10}{'Precio':<10}{'Total':<10}")
    for codigo, cantidad, precio, total in detalles:
        print(f"{codigo:<10}{cantidad:<10}{precio:<10.2f}{total:<10.2f}")
    print("-" * 50)
    print(f"Subtotal: {subtotal:.2f}")
    print(f"ISV (15%): {isv:.2f}")
    print(f"Total General: {total_general:.2f}")

def main():
    # Diccionario de precios: código de artículo -> precio unitario
    precios = {
        1001: 2.50,
        1002: 3.75,
        1003: 1.80,
        1004: 4.20,
        1005: 5.00
    }
    
    print("Sistema de Facturación Automatizada en Ferretería")
    print("=" * 60)
    
    # Ingresar datos de ventas
    ventas = ingresar_ventas()
    
    # Calcular total por artículo basado en los precios
    detalles = calcular_total_por_articulo(ventas, precios)
    
    if not detalles:
        print("No se ingresaron ventas válidas.")
        return

    # Calcular subtotal, ISV y total general
    subtotal = calcular_subtotal(detalles)
    isv, total_general = calcular_total_general(subtotal)
    
    # Mostrar la factura
    mostrar_factura(detalles, subtotal, isv, total_general)

if __name__ == "__main__":
    main()
