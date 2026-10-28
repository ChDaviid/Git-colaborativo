def calcular_precio_final(precio_original, descuento):
    return precio_original - (precio_original * descuento / 100)

precio_original = int(input("Ingrese el precio: "))
descuento = int(input("Ingrese el porcentaje de descuento: "))

print(calcular_precio_final(precio_original, descuento))