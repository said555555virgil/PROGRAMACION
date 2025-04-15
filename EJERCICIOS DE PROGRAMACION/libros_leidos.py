def ingresar_libros(num_estudiantes):
    libros = []
    for i in range(num_estudiantes):
        while True:
            try:
                cantidad = int(input(f"Estudiante {i+1} - Libros leídos: "))
                if cantidad < 0:
                    print("  No puede ser negativo.")
                    continue
                libros.append(cantidad)
                break
            except ValueError:
                print("  Entrada inválida. Intenta nuevamente.")
    return libros

def calcular_total_y_promedio(libros):
    total = sum(libros)
    promedio = total / len(libros)
    return total, promedio

def estudiante_mas_lector(libros):
    max_libros = max(libros)
    estudiante = libros.index(max_libros) + 1
    return estudiante, max_libros

def main():
    num_estudiantes = 20
    print("=== Registro de Libros Leídos por Estudiantes ===")
    
    libros = ingresar_libros(num_estudiantes)
    
    total, promedio = calcular_total_y_promedio(libros)
    mejor_estudiante, max_leidos = estudiante_mas_lector(libros)
    
    print("\n=== Resultados ===")
    for i, cantidad in enumerate(libros):
        print(f"Estudiante {i+1}: {cantidad} libros")

    print(f"\n📚 Total de libros leídos: {total}")
    print(f"📈 Promedio por estudiante: {promedio:.2f}")
    print(f"🏆 Estudiante que leyó más: Estudiante {mejor_estudiante} con {max_leidos} libros")

if __name__ == "__main__":
    main()
