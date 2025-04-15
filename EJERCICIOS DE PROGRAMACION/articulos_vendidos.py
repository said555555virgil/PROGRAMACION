def ingresar_articulos(num_articulos):
    precios = []
    cantidades = []
    
    for i in range(num_articulos):
        while True:
            try:
                precio = float(input(f"Precio del artículo {i+1}: L. "))
                if precio < 0:
                    print("  El precio no puede ser negativo.")
                    continue
                cantidad = int(input(f"Cantidad vendida del artículo {i+1}: "))
                if cantidad < 0:
                    print("  La cantidad no puede ser negativa.")
                    continue
                precios.append(precio)
                cantidades.append(cantidad)
                break
            except ValueError:
                print("  Entrada inválida. Intenta nuevamente.")
    
    return precios, cantidades

def calcular_ganancias(precios, cantidades):
    ganancias = [precio * cantidad for precio, cantidad in zip(precios, cantidades)]
    return ganancias

def articulo_mas_vendido(cantidades):
    max_cantidad = max(cantidades)
    articulo_max = cantidades.index(max_cantidad) + 1
    return articulo_max, max_cantidad

def calcular_ingreso_total(ganancias):
    return sum(ganancias)

def main():
    num_articulos = 100
    print("=== Registro de Artículos Vendidos y Ganancias ===")
    
    precios, cantidades = ingresar_articulos(num_articulos)
    ganancias = calcular_ganancias(precios, cantidades)
    
    articulo_max, max_vendido = articulo_mas_vendido(cantidades)
    ingreso_total = calcular_ingreso_total(ganancias)
    
    print("\n=== Resultados ===")
    for i in range(num_articulos):
        print(f"Artículo {i+1}: Ganancia L. {ganancias[i]:.2f} ({cantidades[i]} unidades vendidas)")
    
    print(f"\n📈 Artículo MÁS vendido: Artículo {articulo_max} con {max_vendido} unidades vendidas")
    print(f"💰 Ingreso total: L. {ingreso_total:.2f}")

if __name__ == "__main__":
    main()
