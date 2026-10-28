equipaje = int(input("Introduce el numero de equipajes que vas a facturar: "))
precio_total = 0

for numero_equipaje in range(1, equipaje + 1):
    peso = float(input(f"¿Cuánto pesa el equipaje {numero_equipaje}? "))

    if peso <= 10:
        precio = 0
        print("Equipaje de mano")
    elif peso <= 20:
        precio = 20
        print("Debes facturar")
    else:
        precio = 20 + (peso - 20) * 5
        print("Debes facturar; sobrepasas el peso límite en", peso - 20, "kg")

    precio_total += precio

Equipajes = []
Equipajes.append((peso, precio))
for equipaje in Equipajes:
    print(f"Peso: {equipaje[0]} kg, Precio: {equipaje[1]} €")
    print("El importe total a pagar es:", precio_total, "€")