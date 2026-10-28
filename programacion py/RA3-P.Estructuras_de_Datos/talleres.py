talleres = [
    (
        "Fotografía",
        ["Ana", "Luis"],
        {"aula": 12, "plazas": 4},
        {"cámara", "tarjeta de memoria"}
    ),
    (
        "Robótica",
        ["Marta"],
        {"aula": 15, "plazas": 3},
        {"portátil", "cable USB"}
    ),
    (
        "Pintura",
        [],
        {"aula": 8, "plazas": 5},
        {"pinceles", "acuarelas", "papel"}
    )
]
while True:
    print("--------------------------------")
    print("1. Mostrar talleres: muestra el nombre, el aula, los alumnos inscritos, las plazas libres y los materiales de todos los talleres.")
    print("2. Inscribir a un alumno: solicita el taller y el nombre. Añádelo si quedan plazas.")
    print("3. Cancelar una inscripción: solicita el taller y el nombre. Elimina al alumno si está inscrito.")
    print("4. Cambiar el aula: solicita el taller y el nuevo número de aula.")
    print("5. Añadir un material: solicita el taller y el material. Añádelo si no existe.")
    print("6. Terminar.")
    print("--------------------------------")

    opcion = int(input("Ingrese el la opción que desea realizar: "))


#Talleres es una lista de tuplas, donde cada tupla representa un taller. Cada taller contiene el nombre del taller (cadena de texto), una lista de participantes (lista), un diccionario con información del aula y plazas (diccionario) y un conjunto de materiales necesarios (conjunto).


# 1. Mostrar talleres: muestra el nombre, el aula, los alumnos inscritos, las plazas libres y los materiales de todos los talleres.
    if opcion == 1:
        print(talleres)


# 2. Inscribir a un alumno: solicita el taller y el nombre. Añádelo si quedan plazas.

    elif opcion == 2:
        nombre_taller = input("Ingrese el nombre del taller al que desea inscribirse: (Fotografía, Robótica, Pintura) ")
        nombre = input("Ingrese su nombre: ")
        for taller in talleres:
            if taller[0] == nombre_taller:
                if taller[2]["plazas"] > 0:
                    taller[1].append(nombre)
                    taller[2]["plazas"] -= 1
                    print("Inscripción realizada con éxito.")
                else:
                    print("No hay plazas disponibles en este taller.")


# 3. Cancelar una inscripción: solicita el taller y el nombre. Elimina al alumno si está inscrito.
    elif opcion == 3:
        nombre_taller = input ("Ingrese el nombre del taller del que desea cancelar la inscripción: (Fotografía, Robótica, Pintura) ")
        nombre = input("Ingrese su nombre: ")
        for taller in talleres:
            if taller[0] == nombre_taller:
                if nombre in taller[1]:
                    taller[1].remove(nombre)
                    taller[2]["plazas"] += 1
                    print("Inscripción cancelada con éxito.")
                else:
                    print("No está inscrito en este taller.")

# Cambiar el aula: solicita el taller y el nuevo número de aula.
    elif opcion == 4:
        nombre_taller = input("Ingrese el nombre del taller al que desea cambiar el aula: (Fotografía, Robótica, Pintura) ")
        nueva_aula = int(input("Ingrese el nuevo número de aula: "))
        for taller in talleres:
            if taller[0] == nombre_taller:
                taller[2]["aula"] = nueva_aula
                print("Aula cambiada con éxito.")
# 5. Añadir un material: solicita el taller y el material. Añádelo si no existe.
    elif opcion == 5:
        nombre_taller = input("Ingrese el nombre del taller al que desea añadir un material: (Fotografía, Robótica, Pintura) ")
        nuevo_material = input("Ingrese el material que desea añadir: ")
        for taller in talleres:
            if taller[0] == nombre_taller:
                if nuevo_material not in taller[3]:
                    taller[3].add(nuevo_material)
                    print("Material añadido con éxito.")
                else:
                    print("El material ya existe en este taller.")

# 6. Terminar.
    elif opcion == 6:
        print("Saliendo del programa...")
        break