mario_kart = {"Ana", "Luis", "Pedro", "Marta", "Hugo"}
minecraft = {"Luis", "Marta", "Sara", "David"}
rocket_league = {"Pedro", "Marta", "David", "Elena"}

while True:
    print("--------------------------------")
    print("1.Mostrar todos los participantes, sin repetir nombres.")
    print("2.Mostrar los participantes comunes a Mario Kart y Minecraft.")
    print("3.Mostrar los participantes inscritos en los tres torneos.")
    print("4.Mostrar los participantes de Mario Kart que no están en Minecraft.")
    print("5.Mostrar los participantes inscritos en Minecraft o Rocket League, pero no en ambos.")
    print("6.Añadir un participante a un torneo.")
    print("7.Eliminar un participante de un torneo.")
    print("8.Consultar en qué torneos está inscrita una persona.")
    print("9. Salir")
    print("--------------------------------")

    opcion = int(input("Ingrese el la opción que desea realizar: "))

    if opcion == 1:
        conjunto_total = mario_kart.union(minecraft).union(rocket_league)
        print(conjunto_total)
    
    elif opcion == 2:
        conjunto_comun = mario_kart.intersection(minecraft)
        print(conjunto_comun)

    elif opcion == 3:
        conjunto_tres = mario_kart.intersection(minecraft, rocket_league)
        print(conjunto_tres)

    elif opcion == 4:
        conjunto_4 = mario_kart.difference(minecraft)
        print(conjunto_4)

    elif opcion == 5:
        conjunto_5 = minecraft.symmetric_difference(rocket_league)
        print(conjunto_5)

    elif opcion == 6:
        conjunto_6 = input("Ingrese el nombre del participante que desea añadir: ")
        torneo = input("Ingrese el torneo al que desea añadirlo (Mario Kart, Minecraft, Rocket League): ")
        if torneo == "Mario Kart":
            mario_kart.add(conjunto_6)
        elif torneo == "Minecraft":
            minecraft.add(conjunto_6)
        else:
            rocket_league.add(conjunto_6)

    elif opcion == 7:
        conjunto_7 = input("Ingrese el nombre del participante que desea eliminar: ")
        torneo = input("Ingrese el torneo del que desea eliminarlo (Mario Kart, Minecraft, Rocket League): ")
        if torneo == "Mario Kart":
            mario_kart.discard(conjunto_7)
        elif torneo == "Minecraft":
            minecraft.discard(conjunto_7)
        else:
            rocket_league.discard(conjunto_7)

    elif opcion == 8:
        conjunto_8 = input("Ingrese el nombre del participante que deseas consultar:")
        if conjunto_8 in mario_kart:
            print(f"{conjunto_8} está inscrito en Mario Kart.")
        if conjunto_8 in minecraft:
            print(f"{conjunto_8} está inscrito en Minecraft.")
        if conjunto_8 in rocket_league:
            print(f"{conjunto_8} está inscrito en Rocket League.")

    elif opcion == 9:
        print("Saliendo del programa...")
        break