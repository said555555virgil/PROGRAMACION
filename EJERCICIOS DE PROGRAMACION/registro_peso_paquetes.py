def ingresar_pesos_paquetes(num_paquetes):
    pesos = []
    for i in range(num_paquetes):
        while True:
            try:
                peso = float(input(f"Peso del paquete {i+1} (kg): "))
                if peso <= 0:
                    print("  El peso debe ser un valor positivo.")
                    continue
                pesos.append(peso)
                break
            except ValueError:
                print("  Entrada inválida. Intenta nuevamente.")
    return pesos

def calcular_peso_total(pesos):
    return sum(pesos)

def encontrar_max_min(pesos):
    max_peso = max(pesos)
    min_peso = min(pesos)
    paquete_max = pesos.index(max_peso) + 1
    paquete_min = pesos.index(min_peso) + 1
    return paquete_max, max_peso, paquete_min, min_peso

def main():
    num_paquetes = 80
    print("=== Registro de Peso de Paquetes ===")
    
    pesos = ingresar_pesos_paquetes(num_paquetes)
    peso_total = calcular_peso_total(pesos)
    paquete_max, max_peso, paquete_min, min_peso = encontrar_max_min(pesos)
    
    print("\n=== Resultados ===")
    print(f"📦 Peso total transportado: {peso_total:.2f} kg")
    print(f"⚖️ Paquete más pesado: Paquete {paquete_max} con {max_peso:.2f} kg")
    print(f"⚖️ Paquete más liviano: Paquete {paquete_min} con {min_peso:.2f} kg")

if __name__ == "__main__":
    main()
