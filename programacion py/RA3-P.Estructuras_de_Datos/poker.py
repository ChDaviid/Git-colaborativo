valores = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
palos = ("♥️", "♦️", "♣️", "♠️")

baraja = []

for valor in valores:
    for palo in palos:
        baraja.append(valor + palo)

print(baraja)
print(f"La baraja contiene {len(baraja)} cartas.")