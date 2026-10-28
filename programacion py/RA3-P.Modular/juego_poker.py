import random
valores = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
palos = ("♥️", "♦️", "♣️", "♠️")

baraja = []

for valor in valores:
    for palo in palos:
        baraja.append(valor + palo)

posicion1 = random.randint(0, len(baraja) - 1)
posicion2 = random.randint(0, len(baraja) - 1)


auxiliar = baraja[posicion1]
baraja[posicion1] = baraja[posicion2]
baraja[posicion2] = auxiliar

def puntuacion_carta(carta):
    for valor in valores:
        if carta[:len(valor)] == valor and carta[len(valor):] in palos:
            if valor == "A":
                return 15
            elif valor == "J":
                return 11
            elif valor == "Q":
                return 12
            elif valor == "K":
                return 13
            else:
                return int(valor)
    return 0


mano = []
for i in range(4):
    mano.append(baraja.pop())

print("\nMano:", mano)

total = 0
puntos = []
for carta in mano:
    p = puntuacion_carta(carta)
    puntos.append(str(p))
    total += p

print("Puntuación:", " + ".join(puntos), "=", total, "puntos.")
print(f"Cartas restantes en la baraja: {len(baraja)}")