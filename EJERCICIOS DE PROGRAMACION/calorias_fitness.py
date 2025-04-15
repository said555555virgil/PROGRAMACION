def ingresar_calorias(num_usuarios, num_dias):
    """
    Registra calorías quemadas por usuario y por día.
    
    Retorna:
      List[List[int]]: Matriz de calorías.
    """
    calorias = []
    for i in range(num_usuarios):
        print(f"\nUsuario {i+1}:")
        fila = []
        for j in range(num_dias):
            while True:
                try:
                    valor = int(input(f"  Día {j+1} (calorías): "))
                    if valor < 0:
                        print("  No puede ser negativo.")
                        continue
                    fila.append(valor)
                    break
                except ValueError:
                    print("  Entrada inválida. Intenta de nuevo.")
        calorias.append(fila)
    return calorias

def calcular_totales_y_promedios(calorias):
    """
    Calcula el total y promedio diario por usuario.
    
    Retorna:
      List[int], List[float]: Totales y promedios por usuario.
    """
    totales = [sum(usuario) for usuario in calorias]
    promedios = [total / len(calorias[0]) for total in totales]
    return totales, promedios

def encontrar_mayor_quemador(totales):
    """
    Encuentra el usuario que más calorías quemó.
    
    Retorna:
      Tuple[int, int]: (número de usuario, total de calorías)
    """
    max_calorias = max(totales)
    usuario = totales.index(max_calorias) + 1
    return usuario, max_calorias

def main():
    num_usuarios = 15
    num_dias = 7

    print("=== Registro de Calorías Semanales ===")
    calorias = ingresar_calorias(num_usuarios, num_dias)

    totales, promedios = calcular_totales_y_promedios(calorias)
    usuario_top, max_total = encontrar_mayor_quemador(totales)

    print("\n=== Resultados ===")
    for i in range(num_usuarios):
        print(f"Usuario {i+1}: {totales[i]} calorías en total | Promedio diario: {promedios[i]:.2f}")

    print(f"\n🔥 Usuario que más calorías quemó: Usuario {usuario_top} con {max_total} calorías")

if __name__ == "__main__":
    main()
