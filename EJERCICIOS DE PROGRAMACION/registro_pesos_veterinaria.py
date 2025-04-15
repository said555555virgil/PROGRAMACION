def ingresar_pesos(num_perros):
    """
    Permite ingresar los pesos de cada uno de los perros.
    
    Parámetros:
      num_perros (int): Número total de perros a pesar.
      
    Retorna:
      List[float]: Lista con el peso de cada perro.
    """
    pesos = []
    for i in range(num_perros):
        while True:
            try:
                peso = float(input(f"Ingrese el peso del perro {i+1}: "))
                if peso <= 0:
                    print("El peso debe ser un número mayor a cero. Intente nuevamente.")
                    continue
                pesos.append(peso)
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")
    return pesos

def calcular_promedio(pesos):
    """
    Calcula el promedio de peso de los perros.
    
    Parámetros:
      pesos (List[float]): Lista con los pesos.
      
    Retorna:
      float: Promedio de peso.
    """
    return sum(pesos) / len(pesos)

def encontrar_peso_maximo(pesos):
    """
    Encuentra el perro con el peso máximo.
    
    Parámetros:
      pesos (List[float]): Lista con los pesos de los perros.
      
    Retorna:
      Tuple[int, float]: Posición (índice + 1) del perro más pesado y su peso.
    """
    peso_max = max(pesos)
    indice_max = pesos.index(peso_max)
    return indice_max + 1, peso_max

def encontrar_peso_minimo(pesos):
    """
    Encuentra el perro con el peso mínimo.
    
    Parámetros:
      pesos (List[float]): Lista con los pesos de los perros.
      
    Retorna:
      Tuple[int, float]: Posición (índice + 1) del perro más liviano y su peso.
    """
    peso_min = min(pesos)
    indice_min = pesos.index(peso_min)
    return indice_min + 1, peso_min

def main():
    num_perros = 25
    print("Registro de Pesos en Veterinaria")
    print("=" * 40)
    
    # Ingresar los pesos
    pesos = ingresar_pesos(num_perros)
    
    # Calcular el promedio de peso
    promedio = calcular_promedio(pesos)
    
    # Determinar el perro más pesado y el más liviano
    perro_mas_pesado, peso_max = encontrar_peso_maximo(pesos)
    perro_mas_liviano, peso_min = encontrar_peso_minimo(pesos)
    
    # Mostrar resultados
    print("\nResultados:")
    print(f"Promedio de peso: {promedio:.2f}")
    print(f"El perro {perro_mas_pesado} es el más pesado con {peso_max:.2f} kg.")
    print(f"El perro {perro_mas_liviano} es el más liviano con {peso_min:.2f} kg.")

if __name__ == "__main__":
    main()
