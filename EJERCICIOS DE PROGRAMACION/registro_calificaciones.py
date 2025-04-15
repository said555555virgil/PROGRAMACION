def ingresar_calificaciones(num_estudiantes):
    """
    Solicita al usuario ingresar la calificación de cada estudiante.
    
    Parámetros:
      num_estudiantes (int): Número de estudiantes a registrar.
      
    Retorna:
      List[float]: Lista con las calificaciones de cada estudiante.
    """
    calificaciones = []
    for i in range(num_estudiantes):
        while True:
            try:
                nota = float(input(f"Ingrese la calificación del estudiante {i+1}: "))
                if nota < 0 or nota > 100:
                    print("La calificación debe estar entre 0 y 100. Intente nuevamente.")
                    continue
                calificaciones.append(nota)
                break
            except ValueError:
                print("Por favor, ingrese un valor numérico válido.")
    return calificaciones

def obtener_nota_maxima(calificaciones):
    """
    Encuentra la nota más alta del grupo.
    
    Parámetros:
      calificaciones (List[float]): Lista de calificaciones.
      
    Retorna:
      float: La calificación máxima.
    """
    return max(calificaciones)

def obtener_nota_minima(calificaciones):
    """
    Encuentra la nota más baja del grupo.
    
    Parámetros:
      calificaciones (List[float]): Lista de calificaciones.
      
    Retorna:
      float: La calificación mínima.
    """
    return min(calificaciones)

def calcular_promedio(calificaciones):
    """
    Calcula el promedio de las calificaciones del grupo.
    
    Parámetros:
      calificaciones (List[float]): Lista de calificaciones.
      
    Retorna:
      float: El promedio.
    """
    return sum(calificaciones) / len(calificaciones)

def contar_aprobados(calificaciones, nota_aprobacion=60):
    """
    Cuenta la cantidad de estudiantes que aprobaron, es decir, cuya calificación es mayor o igual a nota_aprobacion.
    
    Parámetros:
      calificaciones (List[float]): Lista de calificaciones.
      nota_aprobacion (float): Calificación mínima para aprobar (por defecto 60).
      
    Retorna:
      int: Número de estudiantes aprobados.
    """
    return len([nota for nota in calificaciones if nota >= nota_aprobacion])

def main():
    num_estudiantes = 40
    print("Registro de Calificaciones")
    print("=" * 40)
    
    # Ingresar las calificaciones
    calificaciones = ingresar_calificaciones(num_estudiantes)
    
    # Calcular la nota máxima, mínima y el promedio
    nota_maxima = obtener_nota_maxima(calificaciones)
    nota_minima = obtener_nota_minima(calificaciones)
    promedio = calcular_promedio(calificaciones)
    
    # Contar la cantidad de estudiantes aprobados
    aprobados = contar_aprobados(calificaciones)
    
    # Mostrar resultados
    print("\nResultados del examen:")
    print("-" * 30)
    print(f"Nota más alta: {nota_maxima}")
    print(f"Nota más baja: {nota_minima}")
    print(f"Promedio del grupo: {promedio:.2f}")
    print(f"Cantidad de estudiantes aprobados (nota ≥ 60): {aprobados}")

if __name__ == "__main__":
    main()
