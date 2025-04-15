def ingresar_recoleccion(trabajadores):
    recoleccion = []
    for i in range(trabajadores):
        while True:
            try:
                kilos = float(input(f"¿Cuántos kilogramos de granos recolectó el trabajador {i+1}? "))
                if kilos < 0:
                    print("  El número de kilogramos no puede ser negativo.")
                    continue
                recoleccion.append(kilos)
                break
            except ValueError:
                print("  Entrada inválida. Intenta nuevamente.")
    return recoleccion

def calcular_recoleccion_total(recoleccion):
    return sum(recoleccion)

def calcular_promedio(recoleccion):
    return sum(recoleccion) / len(recoleccion)

def identificar_rendimiento_max_min(recoleccion):
    max_recoleccion = max(recoleccion)
    min_recoleccion = min(recoleccion)
    trabajador_max = recoleccion.index(max_recoleccion) + 1
    trabajador_min = recoleccion.index(min_recoleccion) + 1
    return trabajador_max, max_recoleccion, trabajador_min, min_recoleccion

def main():
    trabajadores = 50
    print("=== Registro de Recolección Agrícola por Trabajador ===")
    
    recoleccion = ingresar_recoleccion(trabajadores)
    total_recoleccion = calcular_recoleccion_total(recoleccion)
    promedio_recoleccion = calcular_promedio(recoleccion)
    trabajador_max, max_recoleccion, trabajador_min, min_recoleccion = identificar_rendimiento_max_min(recoleccion)
    
    print("\n=== Resultados ===")
    print(f"🌾 Recolección total: {total_recoleccion:.2f} kg")
    print(f"📊 Promedio de recolección por trabajador: {promedio_recoleccion:.2f} kg")
    print(f"💪 El trabajador con mayor rendimiento recolectó {max_recoleccion:.2f} kg (Trabajador {trabajador_max}).")
    print(f"😞 El trabajador con menor rendimiento recolectó {min_recoleccion:.2f} kg (Trabajador {trabajador_min}).")

if __name__ == "__main__":
    main()
