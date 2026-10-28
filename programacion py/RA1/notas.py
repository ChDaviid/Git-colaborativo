nota = input("¿cuál es tu nota? ")
nota = int(nota)

if nota<6:
    if nota<5:
        if nota<3:
            print("Muy deficiente")
        else:
            print("Insuficiente")
    else:
        print("Suficiente")

else:
    if nota<7:
        print("Bien")
    else:
        if nota<9:
            print("Notable")
        else:
            print("Sobresaliente")