a = int(input("Ingrese un valor para a: "))
b = int(input("Ingrese un valor para b: "))
c = int(input("Ingrese un valor para c: "))

if a < b:
    aux = a
    a = b
    b = aux

if a < c:
    aux = a
    a = c
    c = aux

if b < c:
    aux = b
    b = c
    c = aux

print("Los valores son: a =", a, ", b =", b, ", c =", c)

#El programa pide al usuario ingresar tres valores y luego los ordena de mayor a menor utilizando variables auxiliares para realizar los intercambios necesarios. Finalmente, imprime los valores ordenados.