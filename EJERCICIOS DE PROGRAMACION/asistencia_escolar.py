def ingresar_asistencias(num_estudiantes, num_dias):
    """
    Registra asistencia diaria para cada estudiante.
    
    Retorna:
      List[List[int]]: Matriz con asistencias (1 o 0).
    """
    asistencias = []
    for i in range(num_estudiantes):
        print(f"\nEstudiante {i+1}:")
        fila = []
        for j in range(num_dias):
            while True:
                try:
                    val = int(input(f"  Día {j+1} (1 = asistió, 0 = no asistió): "))
                    if val not in [0, 1]:
                        print("  Solo se permite 1 o 0.")
                        continue
                    fila.append(val)
                    break
                except ValueError:
                    print("  Entrada inválida. Intente de nuevo.")
        asistencias.append(fila)
    return asistencias

def calcular_totales_asistencia(asistencias):
    """
    Suma las asistencias por estudiante.
    
    Retorna:
      List[int]: Lista de totales de asistencia por estudiante.
    """
    return [sum(fila) for fila in asistencias]

def encontrar_max_min(asistencias_totales):
    """
    Encuentra estudiante con más y menos asistencia.
    
    Retorna:
      (int, int), (int, int): (número de estudiante, asistencias) para el mayor y menor.
    """
    max_val = max(asistencias_totales)
    min_val = min(asistencias_totales)
    est_max = asistencias_totales.index(max_val) + 1
    est_min = asistencias_totales.index(min_val) + 1
    return (est_max, max_val), (est_min, min_val)

def main():
    num_estudiantes = 30
    num_dias = 5
    
    print("=== Registro de Asistencia Escolar Semanal ===")
    asistencias = ingresar_asistencias(num_estudiantes, num_dias)
    
    totales = calcular_totales_asistencia(asistencias)
    
    (est_max, max_asist), (est_min, min_asist) = encontrar_max_min(totales)
    
    print("\n=== Resultados ===")
    for i, total in enumerate(totales):
        print(f"Estudiante {i+1}: {total} asistencias")
    
    print(f"\n✅ Estudiante con MÁS asistencias: Estudiante {est_max} ({max_asist} días)")
    print(f"❌ Estudiante con MENOS asistencias: Estudiante {est_min} ({min_asist} días)")

if __name__ == "__main__":
    main()
