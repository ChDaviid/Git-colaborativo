#pedir 5 numeros al usuario
numeros = []
for i in range(5):
    numero = int(input("Ingrese un numero: "))
    numeros.append(numero)

#Detectar el mayor numero
mayor = max(numeros)

#Mostrar el mayor numero
print("El mayor numero ingresado es:", mayor)