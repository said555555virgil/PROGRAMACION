def ingresar_asistencias(num_clases):
    asistencias = []
    for i in range(num_clases):
        while True:
            try:
                cantidad = int(input(f"Asistencia total a la clase {i+1} en la semana: "))
                if cantidad < 0:
                    print("  No puede ser negativo.")
                    continue
                asistencias.append(cantidad)
                break
            except ValueError:
                print("  Entrada inválida. Intenta nuevamente.")
    return asistencias

def encontrar_max_min_asistencia(asistencias):
    max_asistencia = max(asistencias)
    min_asistencia = min(asistencias)
    clase_max = asistencias.index(max_asistencia) + 1
    clase_min = asistencias.index(min_asistencia) + 1
    return clase_max, max_asistencia, clase_min, min_asistencia

def main():
    num_clases = 20
    print("=== Registro de Asistencias a Clases de Gimnasio ===")

    asistencias = ingresar_asistencias(num_clases)
    clase_max, max_asistencia, clase_min, min_asistencia = encontrar_max_min_asistencia(asistencias)

    print("\n=== Resultados ===")
    for i, cantidad in enumerate(asistencias):
        print(f"Clase {i+1}: {cantidad} asistentes en la semana")

    print(f"\n📈 Clase con MAYOR asistencia: Clase {clase_max} con {max_asistencia} personas")
    print(f"📉 Clase con MENOR asistencia: Clase {clase_min} con {min_asistencia} personas")

if __name__ == "__main__":
    main()
