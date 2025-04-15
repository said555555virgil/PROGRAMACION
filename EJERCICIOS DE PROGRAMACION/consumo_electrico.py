def ingresar_consumos(num_casas):
    consumos = []
    for i in range(num_casas):
        while True:
            try:
                consumo = float(input(f"Consumo de la casa {i+1} (kWh): "))
                if consumo < 0:
                    print("  El consumo no puede ser negativo.")
                    continue
                consumos.append(consumo)
                break
            except ValueError:
                print("  Entrada inválida. Intenta nuevamente.")
    return consumos

def calcular_total_promedio(consumos):
    total = sum(consumos)
    promedio = total / len(consumos)
    return total, promedio

def encontrar_max_min(consumos):
    max_consumo = max(consumos)
    min_consumo = min(consumos)
    casa_max = consumos.index(max_consumo) + 1
    casa_min = consumos.index(min_consumo) + 1
    return casa_max, max_consumo, casa_min, min_consumo

def main():
    num_casas = 100
    print("=== Registro de Consumo Eléctrico Diario ===")
    
    consumos = ingresar_consumos(num_casas)
    
    total, promedio = calcular_total_promedio(consumos)
    casa_max, maximo, casa_min, minimo = encontrar_max_min(consumos)

    print("\n=== Resultados ===")
    print(f"⚡ Consumo total: {total:.2f} kWh")
    print(f"📊 Consumo promedio por casa: {promedio:.2f} kWh")
    print(f"🏠 Casa con MAYOR consumo: Casa {casa_max} con {maximo:.2f} kWh")
    print(f"🏠 Casa con MENOR consumo: Casa {casa_min} con {minimo:.2f} kWh")

if __name__ == "__main__":
    main()
