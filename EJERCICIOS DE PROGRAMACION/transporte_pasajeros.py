def ingresar_pasajeros(num_buses):
    """
    Solicita al usuario ingresar la cantidad de pasajeros transportados por cada bus.
    
    Parámetros:
      num_buses (int): Número total de buses.
      
    Retorna:
      List[int]: Lista con la cantidad de pasajeros por cada bus.
    """
    pasajeros = []
    for i in range(num_buses):
        while True:
            try:
                cant = int(input(f"Ingrese la cantidad de pasajeros transportados por el bus {i+1}: "))
                if cant < 0:
                    print("La cantidad no puede ser negativa. Inténtelo de nuevo.")
                    continue
                pasajeros.append(cant)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return pasajeros

def total_pasajeros(pasajeros):
    """
    Calcula el total de pasajeros transportados sumando los valores de la lista.
    
    Parámetros:
      pasajeros (List[int]): Lista con la cantidad de pasajeros por bus.
      
    Retorna:
      int: Total de pasajeros transportados.
    """
    return sum(pasajeros)

def bus_mas_menos(pasajeros):
    """
    Identifica el bus con mayor y menor cantidad de pasajeros.
    
    Parámetros:
      pasajeros (List[int]): Lista con la cantidad de pasajeros por bus.
      
    Retorna:
      Tuple[(int, int), (int, int)]: 
          - El primer elemento es una tupla con (número de bus con más pasajeros, cantidad).
          - El segundo elemento es una tupla con (número de bus con menos pasajeros, cantidad).
    """
    max_pasajeros = max(pasajeros)
    min_pasajeros = min(pasajeros)
    bus_mayor = pasajeros.index(max_pasajeros) + 1  # Sumar 1 para que la numeración inicie en 1.
    bus_menor = pasajeros.index(min_pasajeros) + 1
    return (bus_mayor, max_pasajeros), (bus_menor, min_pasajeros)

def main():
    num_buses = 7
    print("=== Registro de Transporte de Pasajeros ===")
    
    # Ingresar datos de pasajeros por bus
    pasajeros = ingresar_pasajeros(num_buses)
    
    # Calcular el total de pasajeros
    total = total_pasajeros(pasajeros)
    
    # Identificar el bus con mayor y menor cantidad de pasajeros
    (bus_mayor, max_pasajeros), (bus_menor, min_pasajeros) = bus_mas_menos(pasajeros)
    
    # Mostrar resultados
    print("\nResultados:")
    print(f"Total de pasajeros transportados: {total}")
    print(f"El bus {bus_mayor} transportó la mayor cantidad de pasajeros: {max_pasajeros}")
    print(f"El bus {bus_menor} transportó la menor cantidad de pasajeros: {min_pasajeros}")

if __name__ == "__main__":
    main()
