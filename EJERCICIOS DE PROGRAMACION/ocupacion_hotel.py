def ingresar_ocupacion(habitaciones, dias):
    ocupacion = []
    for i in range(habitaciones):
        ocupacion_habitacion = []
        for j in range(dias):
            while True:
                try:
                    ocupada = int(input(f"¿La habitación {i+1} fue ocupada el día {j+1}? (1 para ocupada, 0 para no ocupada): "))
                    if ocupada not in [0, 1]:
                        print("  Solo puedes ingresar 1 (ocupada) o 0 (no ocupada).")
                        continue
                    ocupacion_habitacion.append(ocupada)
                    break
                except ValueError:
                    print("  Entrada inválida. Intenta nuevamente.")
        ocupacion.append(ocupacion_habitacion)
    return ocupacion

def habitacion_mas_ocupada(ocupacion):
    total_ocupaciones = [sum(habitacion) for habitacion in ocupacion]
    max_ocupacion = max(total_ocupaciones)
    habitacion_max = total_ocupaciones.index(max_ocupacion) + 1
    return habitacion_max, max_ocupacion

def calcular_ocupacion_general(ocupacion):
    total_ocupadas = sum([sum(habitacion) for habitacion in ocupacion])
    total_dias = len(ocupacion) * len(ocupacion[0])
    porcentaje_ocupacion = (total_ocupadas / total_dias) * 100
    return porcentaje_ocupacion

def main():
    habitaciones = 20
    dias = 30
    print("=== Registro de Ocupación de Habitaciones de Hotel ===")
    
    ocupacion = ingresar_ocupacion(habitaciones, dias)
    habitacion_max, max_ocupacion = habitacion_mas_ocupada(ocupacion)
    porcentaje_ocupacion = calcular_ocupacion_general(ocupacion)
    
    print("\n=== Resultados ===")
    print(f"🏨 La habitación MÁS ocupada fue la habitación {habitacion_max} con {max_ocupacion} ocupaciones.")
    print(f"📊 El porcentaje de ocupación general fue: {porcentaje_ocupacion:.2f}%")

if __name__ == "__main__":
    main()
