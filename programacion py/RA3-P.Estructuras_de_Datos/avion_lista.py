numero_equipajes = int(input("Introduce el numero de equipajes que vas a facturar: "))
equipajes = []

for numero_equipaje in range(1, numero_equipajes + 1):
    peso = float(input(f"¿Cuánto pesa el equipaje {numero_equipaje}? "))

    if peso <= 10:
        precio = 0
    elif peso <= 20:
        precio = 20
    else:
        precio = 20 + (peso - 20) * 5

    equipaje = {
        "peso": peso,
        "precio": precio
    }
    equipajes.append(equipaje)

precio_total = 0
for equipaje in equipajes:
    print(f"Peso: {equipaje['peso']} kg, Precio: {equipaje['precio']} €")
    precio_total += equipaje["precio"]

print("El importe total a pagar es:", precio_total, "€")
