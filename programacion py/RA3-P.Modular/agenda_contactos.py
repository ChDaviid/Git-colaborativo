agenda = []

def añadir_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto: ")
    email = input("Ingrese el email del contacto: ")
    telefono = input("Ingrese el teléfono del contacto: ")
    agenda.append({"nombre": nombre, "email": email, "telefono": telefono})
    print("Contacto añadido correctamente.")

def mostrar_agenda(agenda):
    for contacto in agenda:
        print("---------------------------------")
        print(f"Nombre: {contacto['nombre']}\nEmail: {contacto['email']}\nTeléfono: {contacto['telefono']}")
    print("---------------------------------")

def borrar_contacto(agenda):
    print("---------------------------------")
    nombre = input("Ingrese el nombre del contacto que desea borrar: ").lower()
    for contacto in agenda:
        if contacto["nombre"].lower() == nombre:
            agenda.remove(contacto)
            print("Contacto borrado correctamente.")
            print("---------------------------------")
        else:
            print("Contacto no encontrado.")
            print("---------------------------------")

def buscar_contacto(agenda):
    print("---------------------------------")
    nombre = input("Ingrese el nombre del contacto que desea buscar: ").lower()
    for contacto in agenda:
        if contacto["nombre"].lower() == nombre:
            print(f"Nombre: {contacto['nombre']}\nEmail: {contacto['email']}\nTeléfono: {contacto['telefono']}")
            print("---------------------------------")
        else:
            print("Contacto no encontrado.")
            print("---------------------------------")



def buscar_letra(letra):
    print("---------------------------------")
    letra = input("Ingrese la letra inicial del contacto que desea buscar: ").lower()
    for contacto in agenda:
        if contacto["nombre"].lower().startswith(letra):
            print(f"Nombre: {contacto['nombre']}\nEmail: {contacto['email']}\nTeléfono: {contacto['telefono']}")
            print("---------------------------------")
        else:
            print("No se encontraron contactos con esa letra inicial.")
            print("---------------------------------")


def salir():
    print("Saliendo de la agenda de contactos.")
    exit()



while True:
    print("\nAgenda de Contactos")
    print("1. Añadir contacto")
    print("2. Mostrar agenda")
    print("3. Borrar contacto")
    print("4. Buscar contacto por nombre")
    print("5. Buscar contactos por letra inicial")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        añadir_contacto(agenda)

    elif opcion == "2":
       mostrar_agenda(agenda)

    elif opcion == "3":
        borrar_contacto(agenda)

    elif opcion == "4":
        buscar_contacto(agenda)

    elif opcion == "5":
        buscar_letra(agenda)

    elif opcion == "6":
        salir()
        break

    