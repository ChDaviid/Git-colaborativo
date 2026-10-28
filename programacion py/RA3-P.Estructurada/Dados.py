import random

input("Presiona Enter para lanzar los dados...")

puntuacion = 0

print("Has lanzado los dados:")
for i in range(10):
    dado = random.randint(1, 6)
    print("Has sacado un", dado)

    if dado == 6:
        puntuacion += 12
    else:
        puntuacion += dado

print("¡Felicidades! Por cada 6, has ganado 12 puntos extra." )
print("Puntuación total:", puntuacion)

