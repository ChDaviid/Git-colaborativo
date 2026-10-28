# Lista de coches
coches = []
coches.append("Toyota")
coches.append("Honda")
coches.append("Ford")
coches.append("Chevrolet")

# Pedir modelos hasta que el usuario escriba "salir"
while True:
    modelo = input("Introduce un modelo de coche (o escribe 'salir' para terminar): ")
    if modelo == "salir":
        break

    coches.append(modelo)
    posicion = coches.index(modelo)
    print(f"El coche {modelo} está en la posición: {posicion}")
