import os

carpeta = os.path.dirname(os.path.abspath(__file__))
ruta = os.path.join(carpeta, 'invasion_zombi_madrid.csv')
with open(ruta, "r", encoding="utf-8") as fichero:
    filas = fichero.read().splitlines()

lista_zombis = [fila.split(";") for fila in filas[1:] if fila.strip()]

def mostrar_zombis(lista):
    for zombi in lista:
        print(zombi)


def buscar_zombi_id(lista, id_zombi):
    for zombi in lista: 
        if zombi[0] == id_zombi:
            return zombi
    return None


def mostrar_zombi_zona(lista, zona):
    for zombi in lista:
        if zombi[2] == zona:
            print(zombi)

def zombi_tipo(lista, tipo):
    for zombi in lista:
        if zombi[3] == tipo:
            print(zombi)


def contar_zombis_estado(lista, estado):
    contador = 0
    for zombi in lista:
        if zombi[7] == estado:
            contador += 1
    return contador

def zombis_peligrosos(lista):
    for zombi in lista:
        if int(zombi[6]) >= 7:
            print(zombi)


def velocidad_zombi_media(lista):
    suma_velocidad = 0
    for zombi in lista:
        suma_velocidad += int(zombi[5])
    velocidad_media = suma_velocidad / len(lista)
    return velocidad_media


def humanos_infectados_total(lista):
    total_infectados = 0
    for zombi in lista:
        total_infectados += int(zombi[8])
    return total_infectados


def estadistica_zonas(lista):
    zona = input("Introduzca la zona: ").strip()
    zombis_zona = [zombi for zombi in lista if zombi[2] == zona]

    if not zombis_zona:
        print(f"No hay zombis registrados en la zona {zona}.")
        return

    zombis_activos = sum(1 for zombi in zombis_zona if zombi[7] == "Activo")
    peligrosidad_media = (
        sum(int(zombi[6]) for zombi in zombis_zona) / len(zombis_zona)
    )
    humanos_infectados = sum(int(zombi[8]) for zombi in zombis_zona)

    print(f"\nEstadísticas de la zona {zona}:")
    print(f"Número total de zombis: {len(zombis_zona)}")
    print(f"Número de zombis activos: {zombis_activos}")
    print(f"Peligrosidad media: {peligrosidad_media:.2f}")
    print(f"Número total de humanos infectados: {humanos_infectados}")


def ejecutar_menu(lista):
    while True:
        print("\nOpciones:")
        print("1. Mostrar todos los zombis")
        print("2. Buscar zombi por ID")
        print("3. Mostrar zombis por zona")
        print("4. Mostrar zombis por tipo")
        print("5. Contar zombis por estado")
        print("6. Mostrar zombis peligrosos")
        print("7. Calcular velocidad media de los zombis")
        print("8. Calcular total de humanos infectados")
        print("9. Mostrar estadísticas de una zona")
        print("10. Salir del programa")

        opcion = input("Seleccione una opción (1-10): ")

        if opcion == "1":
            print("---------------------------------")
            mostrar_zombis(lista)
            print("---------------------------------")
        elif opcion == "2":
            id_zombi = input("Introduzca el ID del zombi: ")
            zombi = buscar_zombi_id(lista, id_zombi)
            print("---------------------------------")
            print(zombi if zombi else "No se ha encontrado ese zombi.")
            print("---------------------------------")
        elif opcion == "3":
            print("---------------------------------")
            mostrar_zombi_zona(lista, input("Introduzca la zona: "))
            print("---------------------------------")
        elif opcion == "4":
            print("---------------------------------")
            zombi_tipo(lista, input("Introduzca el tipo: "))
            print("---------------------------------")
        elif opcion == "5":
            estado = input("Introduzca el estado: ")
            print("---------------------------------")
            print(f"Zombis con estado {estado}: {contar_zombis_estado(lista, estado)}")
            print("---------------------------------")
        elif opcion == "6":
            print("---------------------------------")
            zombis_peligrosos(lista)
            print("---------------------------------")
        elif opcion == "7":
            print("---------------------------------")
            print(f"Velocidad media: {velocidad_zombi_media(lista)}")
            print("---------------------------------")
        elif opcion == "8":
            print("---------------------------------")
            print(f"Humanos infectados: {humanos_infectados_total(lista)}")
            print("---------------------------------")
        elif opcion == "9":
            print("---------------------------------")
            estadistica_zonas(lista)
            print("---------------------------------")
        elif opcion == "10":
            print("---------------------------------")
            print("Saliendo del programa...")
            print("---------------------------------")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    ejecutar_menu(lista_zombis)




