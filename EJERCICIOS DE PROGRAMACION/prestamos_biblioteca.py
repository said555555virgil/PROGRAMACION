def ingresar_prestamos(num_libros):
    prestamos = []
    for i in range(num_libros):
        while True:
            try:
                cantidad = int(input(f"¿Cuántas veces se prestó el libro {i+1} durante el mes? "))
                if cantidad < 0:
                    print("  El número de préstamos no puede ser negativo.")
                    continue
                prestamos.append(cantidad)
                break
            except ValueError:
                print("  Entrada inválida. Intenta nuevamente.")
    return prestamos

def libro_mas_menos_prestado(prestamos):
    max_prestado = max(prestamos)
    min_prestado = min(prestamos)
    libro_max = prestamos.index(max_prestado) + 1
    libro_min = prestamos.index(min_prestado) + 1
    return libro_max, max_prestado, libro_min, min_prestado

def main():
    num_libros = 100
    print("=== Registro de Préstamos en Biblioteca ===")
    
    prestamos = ingresar_prestamos(num_libros)
    libro_max, max_prestado, libro_min, min_prestado = libro_mas_menos_prestado(prestamos)
    
    print("\n=== Resultados ===")
    print(f"📚 El libro MÁS prestado fue el libro {libro_max} con {max_prestado} préstamos.")
    print(f"📚 El libro MENOS solicitado fue el libro {libro_min} con {min_prestado} préstamos.")

if __name__ == "__main__":
    main()
