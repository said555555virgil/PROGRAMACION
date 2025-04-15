def ingresar_huevos(num_gallinas):
    """
    Solicita al usuario ingresar la cantidad de huevos recolectados por cada gallina.
    
    Parámetros:
      num_gallinas (int): Número total de gallinas.
      
    Retorna:
      List[int]: Lista con la cantidad de huevos recolectados por cada gallina.
    """
    huevos = []
    for i in range(num_gallinas):
        while True:
            try:
                cantidad = int(input(f"Ingrese la cantidad de huevos recolectados por la gallina {i+1}: "))
                if cantidad < 0:
                    print("Por favor, ingrese un número no negativo.")
                    continue
                huevos.append(cantidad)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return huevos

def encontrar_maximo(huevos):
    """
    Encuentra la gallina que produjo la mayor cantidad de huevos.
    
    Parámetros:
      huevos (List[int]): Lista con la cantidad de huevos por gallina.
      
    Retorna:
      Tuple[int, int]: Indice de la gallina (empezando en 1) y la cantidad máxima de huevos.
    """
    max_huevos = max(huevos)
    indice = huevos.index(max_huevos)
    return indice + 1, max_huevos

def encontrar_minimo(huevos):
    """
    Encuentra la gallina que produjo la menor cantidad de huevos.
    
    Parámetros:
      huevos (List[int]): Lista con la cantidad de huevos por gallina.
      
    Retorna:
      Tuple[int, int]: Indice de la gallina (empezando en 1) y la cantidad mínima de huevos.
    """
    min_huevos = min(huevos)
    indice = huevos.index(min_huevos)
    return indice + 1, min_huevos

def calcular_total_huevos(huevos):
    """
    Calcula el total de huevos recolectados sumando los valores de la lista.
    
    Parámetros:
      huevos (List[int]): Lista con la cantidad de huevos por gallina.
      
    Retorna:
      int: Total de huevos recolectados.
    """
    return sum(huevos)

def main():
    num_gallinas = 50
    print("Control de Huevos Recolectados")
    print("=" * 40)
    
    # Ingreso de datos
    huevos = ingresar_huevos(num_gallinas)
    
    # Encontrar la gallina que más y menos produjo huevos
    gallina_max, huevos_max = encontrar_maximo(huevos)
    gallina_min, huevos_min = encontrar_minimo(huevos)
    
    # Calcular el total recolectado
    total_huevos = calcular_total_huevos(huevos)
    
    # Mostrar resultados
    print("\nResultados:")
    print(f"La gallina {gallina_max} produjo la mayor cantidad de huevos: {huevos_max}.")
    print(f"La gallina {gallina_min} produjo la menor cantidad de huevos: {huevos_min}.")
    print(f"Total de huevos recolectados: {total_huevos}")

if __name__ == "__main__":
    main()
