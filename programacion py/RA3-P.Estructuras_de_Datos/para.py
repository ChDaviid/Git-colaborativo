#Pedir numero
numero = int(input("Ingrese un numero: "))
#Cuenta atras
for i in range(numero, 0, -1):
    print(i)
#sumar numeros mostrando el resultado
suma = 0
for i in range(1, numero + 1):
    suma += i

print("La suma total es de:", suma)