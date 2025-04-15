def ingresar_ventas():
    """
    Permite ingresar las ventas diarias de la cafetería.
    Cada venta consta del código del producto y el precio.
    La entrada se termina al ingresar 'fin' en el código.
    
    Retorna:
      List[Tuple[int, float]]: Lista de ventas con tuplas (código, precio)
    """
    ventas = []
    print("Ingrese los datos de cada venta. Para terminar, escriba 'fin' en el código del producto.")
    while True:
        codigo_input = input("Código de producto (1-200 o 'fin' para terminar): ")
        if codigo_input.lower() == "fin":
            break
        try:
            codigo = int(codigo_input)
            if not 1 <= codigo <= 200:
                print("El código debe estar entre 1 y 200.")
                continue
            precio = float(input("Precio del producto: "))
        except ValueError:
            print("Por favor, ingrese datos numéricos válidos.")
            continue
        ventas.append((codigo, precio))
    return ventas

def contar_productos(ventas):
    """
    Cuenta cuántas veces se vendió cada producto.
    
    Parámetros:
      ventas (List[Tuple[int, float]]): Lista de ventas registradas.
      
    Retorna:
      dict: Diccionario en el que la clave es el código del producto y el valor es la cantidad de ventas.
    """
    conteo = {}
    for codigo, _ in ventas:
        if codigo in conteo:
            conteo[codigo] += 1
        else:
            conteo[codigo] = 1
    return conteo

def calcular_ingreso_total(ventas):
    """
    Calcula el ingreso total del día sumando el precio de cada venta.
    
    Parámetros:
      ventas (List[Tuple[int, float]]): Lista de ventas registradas.
      
    Retorna:
      float: Ingreso total del día.
    """
    total = sum(precio for _, precio in ventas)
    return total

def mostrar_resultados(conteo, ingreso_total):
    """
    Muestra el conteo de ventas por producto y el ingreso total del día.
    """
    print("\nConteo de ventas por producto:")
    print("-" * 40)
    # Se muestran solo los productos que se vendieron (en orden de código)
    for codigo in sorted(conteo.keys()):
        print(f"Producto {codigo}: {conteo[codigo]} ventas")
    print("-" * 40)
    print(f"Ingreso total del día: {ingreso_total:.2f}")

def main():
    print("Sistema de Ventas Diarias en una Cafetería")
    print("=" * 50)
    
    # Ingreso de ventas
    ventas = ingresar_ventas()
    
    # Si no se ingresaron ventas, se finaliza la ejecución
    if not ventas:
        print("No se registraron ventas.")
        return

    # Obtener conteo de cada producto y calcular ingreso total
    conteo = contar_productos(ventas)
    ingreso_total = calcular_ingreso_total(ventas)
    
    # Mostrar los resultados
    mostrar_resultados(conteo, ingreso_total)

if __name__ == "__main__":
    main()
