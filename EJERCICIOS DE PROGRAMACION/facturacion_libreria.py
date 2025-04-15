def ingresar_compras():
    """
    Permite ingresar los datos de la compra.
    Cada registro consiste en el código del producto y la cantidad a comprar.
    La entrada finaliza cuando el usuario ingresa 'fin' en el campo del código.
    
    Retorna:
      List[Tuple[int, int]]: Lista con los pares (código, cantidad)
    """
    compras = []
    print("Ingrese los datos de la compra. Para finalizar, escriba 'fin' en el código del producto.")
    while True:
        codigo_input = input("Código del producto: ")
        if codigo_input.lower() == "fin":
            break
        try:
            codigo = int(codigo_input)
        except ValueError:
            print("Ingrese un código numérico válido.")
            continue
        try:
            cantidad = int(input("Cantidad a comprar: "))
        except ValueError:
            print("Ingrese una cantidad numérica válida.")
            continue
        compras.append((codigo, cantidad))
    return compras

def procesar_compras(compras, productos, tasa_descuento=0.10):
    """
    Procesa cada compra: verifica que el producto exista, calcula el subtotal y aplica descuento si la
    cantidad comprada es mayor a 10 unidades.
    
    Parámetros:
      compras (List[Tuple[int, int]]): Lista de compras con (código, cantidad)
      productos (dict): Diccionario donde la clave es el código del producto y el valor es el precio unitario.
      tasa_descuento (float): Tasa de descuento a aplicar si se compran más de 10 unidades (por defecto 10%).
      
    Retorna:
      List[Tuple[int, int, float, float, float]]: Lista de detalles con
          (código, cantidad, precio_unitario, descuento_aplicado, subtotal_producto)
    """
    detalles = []
    for codigo, cantidad in compras:
        if codigo in productos:
            precio_unitario = productos[codigo]
            subtotal_producto = precio_unitario * cantidad
            descuento_aplicado = 0
            if cantidad > 10:
                descuento_aplicado = subtotal_producto * tasa_descuento
                subtotal_producto -= descuento_aplicado
            detalles.append((codigo, cantidad, precio_unitario, descuento_aplicado, subtotal_producto))
        else:
            print(f"El código {codigo} no se encontró en el catálogo.")
    return detalles

def calcular_subtotal(detalles):
    """
    Calcula el subtotal de la factura sumando el subtotal de cada producto.
    
    Parámetros:
      detalles (List[Tuple[int, int, float, float, float]]): Detalles de cada compra.
      
    Retorna:
      float: Subtotal de la factura.
    """
    return sum(detalle[4] for detalle in detalles)

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
    Muestra en pantalla el detalle de la factura, incluyendo cada producto, el subtotal, ISV y el total general.
    """
    print("\nDetalle de la Factura:")
    print("-" * 70)
    print(f"{'Código':<10}{'Cantidad':<10}{'Precio':<10}{'Desc.':<10}{'Subtotal':<10}")
    for codigo, cantidad, precio, descuento, subprod in detalles:
        print(f"{codigo:<10}{cantidad:<10}{precio:<10.2f}{descuento:<10.2f}{subprod:<10.2f}")
    print("-" * 70)
    print(f"Subtotal general: {subtotal:.2f}")
    print(f"ISV (15%): {isv:.2f}")
    print(f"Total general: {total_general:.2f}")

def main():
    # Definimos un diccionario de productos: código -> precio unitario.
    # Para efectos del ejemplo, se muestran algunos productos, pero se asume que existen 100 productos.
    productos = {
        1: 15.50,
        2: 25.00,
        3: 9.75,
        4: 13.20,
        5: 20.00,
        # Se pueden agregar más productos hasta 100...
    }
    
    print("Sistema de Facturación en Librería")
    print("=" * 60)
    
    # Ingresar las compras del cliente
    compras = ingresar_compras()
    
    # Procesar las compras aplicando descuento si corresponde
    detalles = procesar_compras(compras, productos)
    
    if not detalles:
        print("No se registraron compras válidas.")
        return
    
    # Calcular el subtotal de la factura
    subtotal = calcular_subtotal(detalles)
    
    # Calcular ISV y total general
    isv, total_general = calcular_total_general(subtotal)
    
    # Mostrar la factura completa
    mostrar_factura(detalles, subtotal, isv, total_general)

if __name__ == "__main__":
    main()
