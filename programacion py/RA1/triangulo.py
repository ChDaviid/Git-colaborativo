#Preguntar por la medida de los lados
base = int(input("Cuanto mide la base "))
lado1 = int(input("Cuanto mide el lado1 "))
lado2 = int(input("Cuanto mide el lado2 "))

#Condiciones del triangulo
if base==lado1 and lado2==base:
    print("El triangulo es Equilátero")
elif base==lado1 or base==lado2 or lado1==lado2 or lado1==base or lado2==base:
    print("El triangulo es Isósceles")
else:
    print("El triangulo es Escaleno")
