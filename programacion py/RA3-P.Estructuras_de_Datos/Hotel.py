habitaciones = [
    {
        "numero": 101,
        "planta": 1,
        "tipo": "Individual",
        "precio": 50,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 102,
        "planta": 1,
        "tipo": "Doble",
        "precio": 80,
        "ocupadaPor": {
            "nombre": "Ana García",
            "dni": "12345678A",
            "fechaEntrada": "2026-10-07",
            "noches": 3
        }
    },
    {
        "numero": 103,
        "planta": 1,
        "tipo": "Doble",
        "precio": 80,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 104,
        "planta": 1,
        "tipo": "Suite",
        "precio": 150,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 105,
        "planta": 1,
        "tipo": "Individual",
        "precio": 50,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 201,
        "planta": 2,
        "tipo": "Doble",
        "precio": 85,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 202,
        "planta": 2,
        "tipo": "Suite",
        "precio": 160,
        "ocupadaPor": {
            "nombre": "Carlos López",
            "dni": "87654321B",
            "fechaEntrada": "2026-10-06",
            "noches": 5
        }
    },
    {
        "numero": 203,
        "planta": 2,
        "tipo": "Individual",
        "precio": 55,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 204,
        "planta": 2,
        "tipo": "Doble",
        "precio": 85,
        "ocupadaPor": "Libre"
    },
    {
        "numero": 205,
        "planta": 2,
        "tipo": "Suite",
        "precio": 160,
        "ocupadaPor": "Libre"
    }
]

recaudacion = 0

opcion = "9"
while opcion!="6":
    print("\n===== GESTIÓN DEL HOTEL =====")
    print("1. Registrar entrada")
    print("2. Registrar salida")
    print("3. Listar habitaciones ocupadas")
    print("4. Listar habitaciones libres")
    print("5. Resumen del hotel")
    print("6. Terminar programa")
    opcion = input("Selecciona una opción: ")
    match opcion:
        case "1":
            print("REGISTRAR ENTRADA")
            for i in range(len(habitaciones)):
                if habitaciones[i]["ocupadaPor"] == "Libre":
                    print(i, "- Habitación:", habitaciones[i]["numero"],
                          "- Planta:", habitaciones[i]["planta"],
                          "- Tipo:", habitaciones[i]["tipo"],
                          "- Precio:", habitaciones[i]["precio"], "€")
            opcionHabitacion = int(input("Selecciona habitación: "))

            if habitaciones[opcionHabitacion]["ocupadaPor"]!="Libre":
                print("La habitación está ocupada por", habitaciones[opcionHabitacion]["ocupadaPor"]["nombre"])
            else:
                nombre = input("Nombre del cliente: ")
                dni = input("DNI: ")
                fecha = input("Fecha de entrada (AAAA-MM-DD): ")
                noches = int(input("Número de noches: "))

                habitaciones[opcionHabitacion]["ocupadaPor"] = {
                    "nombre": nombre,
                    "dni": dni,
                    "fechaEntrada": fecha,
                    "noches": noches
                }

                print("Entrada registrada correctamente.")

        case "2":
            print("REGISTRAR SALIDA")
            for i in range(len(habitaciones)):
                if habitaciones[i]["ocupadaPor"] != "Libre":
                    print(i, "- Habitación:", habitaciones[i]["numero"],
                          "- Tipo:", habitaciones[i]["tipo"],
                          "- Cliente:", habitaciones[i]["ocupadaPor"]["nombre"])
               
            opcionHabitacion = int(input("Selecciona una habitación: "))

            if habitaciones[opcionHabitacion]["ocupadaPor"]=="Libre":
                print("Habitación libre, no se puede registrar la salida.")
            else:
                importe = habitaciones[opcionHabitacion]["precio"] * habitaciones[opcionHabitacion]["ocupadaPor"]["noches"]
                recaudacion = recaudacion + importe

                print("Importe de la estancia:", importe, "€")

                habitaciones[opcionHabitacion]["ocupadaPor"] = "Libre"

                print("Salida registrada correctamente.")

        case "3":
            print("LISTAR HABITACIONES OCUPADAS")
            for h in habitaciones:
                if h["ocupadaPor"]!="Libre":
                    cliente = h["ocupadaPor"]
                    print("\nHabitación:", h["numero"])
                    print("Tipo:", h["tipo"])
                    print("Precio por noche:", h["precio"], "€")
                    print("Cliente:", cliente["nombre"])
                    print("DNI:", cliente["dni"])
                    print("Fecha de entrada:", cliente["fechaEntrada"])
                    print("Noches:", cliente["noches"])
        case "4":
            print("LISTAR HABITACIONES LIBRES")
            for h in habitaciones:
                if h["ocupadaPor"]=="Libre":
                    print("\nHabitación:", h["numero"])
                    print("Planta:", h["planta"])
                    print("Tipo:", h["tipo"])
                    print("Precio por noche:", h["precio"], "€")
        case "5":
            print("RESUMEN DEL HOTEL")
            libres = 0
            ocupadas = 0

            for habitacion in habitaciones:
                if habitacion["ocupadaPor"] == "Libre":
                    libres = libres + 1
                else:
                    ocupadas = ocupadas + 1

            print("Habitaciones libres:", libres)
            print("Habitaciones ocupadas:", ocupadas)
            print("Recaudación acumulada:", recaudacion, "€")
        case "6":
            print("FIN DEL PROGRAMA")