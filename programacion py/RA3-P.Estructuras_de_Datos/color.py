#Lista colores
colores = ["rojo", "verde", "azul", "amarillo", "naranja", "violeta"]
colores.sort ()
print(colores)
#Generar un color aleatorio
import random
color = random.randint(0, 5)
print("El color aleatorio es: ", colores[color])