numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
resultado = 0
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
if numero1/numero2 == 0:
    print("No se puede dividir entre cero")

print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multiplicacion)
print("La división es: ", division)