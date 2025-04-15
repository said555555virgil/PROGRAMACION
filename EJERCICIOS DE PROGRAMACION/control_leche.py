def ingresar_produccion(num_vacas):
    produccion = [10]
    for i in range(num_vacas):
        litros = float(input(f"Ingrese los litros de leche producidos por la vaca {i+1}: "))
        produccion.append(litros)
    return produccion

def obtener_maximo(produccion):
    max_litros = max(produccion)
    indice = produccion.index(max_litros)
    return indice + 1, max_litros  # +1 porque la vaca se numera desde 1

def obtener_minimo(produccion):
    min_litros = min(produccion)
    indice = produccion.index(min_litros)
    return indice + 1, min_litros

def calcular_promedio(produccion):
    return sum(produccion) / len(produccion)

def main():
    num_vacas = 30
    produccion = ingresar_produccion(num_vacas)

    dia_max, litros_max = obtener_maximo(produccion)
    dia_min, litros_min = obtener_minimo(produccion)
    promedio = calcular_promedio(produccion)

    print(f"\nLa vaca que más produjo fue la número {dia_max} con {litros_max:.2f} litros.")
    print(f"La vaca que menos produjo fue la número {dia_min} con {litros_min:.2f} litros.")
    print(f"El promedio de producción diaria es de {promedio:.2f} litros.")

# Ejecutar el programa
main()



