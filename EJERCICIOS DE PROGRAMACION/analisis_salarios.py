def ingresar_salarios(num_empleados):
    salarios = []
    for i in range(num_empleados):
        while True:
            try:
                salario = float(input(f"Salario del empleado {i+1}: L. "))
                if salario < 0:
                    print("  El salario no puede ser negativo.")
                    continue
                salarios.append(salario)
                break
            except ValueError:
                print("  Entrada inválida. Intenta nuevamente.")
    return salarios

def calcular_promedio(salarios):
    return sum(salarios) / len(salarios)

def encontrar_max_min(salarios):
    max_salario = max(salarios)
    min_salario = min(salarios)
    return max_salario, min_salario

def contar_mayores_que_promedio(salarios, promedio):
    return sum(1 for s in salarios if s > promedio)

def main():
    num_empleados = 50
    print("=== Análisis de Salarios de Empleados ===")
    
    salarios = ingresar_salarios(num_empleados)
    promedio = calcular_promedio(salarios)
    max_salario, min_salario = encontrar_max_min(salarios)
    mayores_al_promedio = contar_mayores_que_promedio(salarios, promedio)

    print("\n=== Resultados ===")
    print(f"📊 Salario promedio: L. {promedio:.2f}")
    print(f"💵 Mayor salario: L. {max_salario:.2f}")
    print(f"💸 Menor salario: L. {min_salario:.2f}")
    print(f"🧍‍♂️ Empleados que ganan más del promedio: {mayores_al_promedio}")

if __name__ == "__main__":
    main()
