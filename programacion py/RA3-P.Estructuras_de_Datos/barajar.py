import random

valores = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
palos = ("♥️", "♦️", "♣️", "♠️")

baraja = []

for valor in valores:
    for palo in palos:
        baraja.append(valor + palo)

print(baraja)
print(f"La baraja contiene {len(baraja)} cartas.")

# Barajar: intercambiar dos posiciones al azar usando una variable auxiliar
posicion1 = random.randint(0, len(baraja) - 1)
posicion2 = random.randint(0, len(baraja) - 1)

print(f"\nSe intercambian las posiciones {posicion1} y {posicion2}.")

auxiliar = baraja[posicion1]
baraja[posicion1] = baraja[posicion2]
baraja[posicion2] = auxiliar

# Mostrar la baraja de nuevo para comprobar el resultado
print("\nBaraja después de barajar:")
print(baraja)