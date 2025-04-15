def registrar_ventas():
    """
    Registra la cantidad de galones vendidos cada hora durante 24 horas.
    
    Retorna:
      List[float]: Lista con la cantidad de galones vendidos en cada hora.
    """
    ventas = []
    print("Ingrese los galones vendidos por cada hora (1 a 24):")
    for hora in range(1, 25):
        while True:
            try:
                galones = float(input(f"Hora {hora}: "))
                if galones < 0:
                    print("El valor debe ser positivo. Intente nuevamente.")
                    continue
                ventas.append(galones)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return ventas

def encontrar_maximo(ventas):
    """
    Determina la hora en la que se vendió la mayor cantidad de galones.
    
    Parámetros:
      ventas (List[float]): Lista de galones vendidos por hora.
      
    Retorna:
      Tuple[int, float]: La hora (1-24) con la mayor venta y el valor correspondiente.
    """
    max_venta = max(ventas)
    # Se suma 1 al índice para que la hora inicie en 1 y no en 0.
    hora_max = ventas.index(max_venta) + 1
    return hora_max, max_venta

def encontrar_minimo(ventas):
    """
    Determina la hora en la que se vendió la menor cantidad de galones.
    
    Parámetros:
      ventas (List[float]): Lista de galones vendidos por hora.
      
    Retorna:
      Tuple[int, float]: La hora (1-24) con la menor venta y el valor correspondiente.
    """
    min_venta = min(ventas)
    hora_min = ventas.index(min_venta) + 1
    return hora_min, min_venta

def total_galones(ventas):
    """
    Calcula el total de galones vendidos en el día.
    
    Parámetros:
      ventas (List[float]): Lista de galones vendidos por hora.
      
    Retorna:
      float: Total de galones vendidos.
    """
    return sum(ventas)

def main():
    print("=== Control de Ventas de Gasolina ===")
    ventas = registrar_ventas()
    
    hora_max, max_valor = encontrar_maximo(ventas)
    hora_min, min_valor = encontrar_minimo(ventas)
    total = total_galones(ventas)
    
    print("\nResultados:")
    print(f"Hora con mayor venta: {hora_max} (se vendieron {max_valor:.2f} galones).")
    print(f"Hora con menor venta: {hora_min} (se vendieron {min_valor:.2f} galones).")
    print(f"Total de galones vendidos en el día: {total:.2f}")

if __name__ == "__main__":
    main()
