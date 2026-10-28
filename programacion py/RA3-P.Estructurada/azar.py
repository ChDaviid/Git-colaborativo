#Primero eliges un numero
dinero = int(input("Cuánto quieres apostar "))
numero_apuesta = int(input("Que numero eliges (1, 3) "))
#azar
import random
numero = random.randint(1,3)
print(numero)
#Dinero apostado
if numero_apuesta==numero:
    print("Has ganado: ")
    dinero = dinero*36
else:
    print("Has perdido")
    dinero = dinero-dinero

print("has ganado:", dinero)
#Opciones
saldo = 100
opcion = ""

while opcion!="4":
    print("1. Doblar")
    print("2. Repetir")
    print("3. All in")
    print("4. Terminar")
    opcion = input("Elige opcion (1,2,3,4): ")

match opcion:
    case "1":
        dinero = dinero*2
    case "2":
        dinero = dinero
    case "3":
        dinero = saldo
    case "4":
        print("Adios")
    case _:
        print("opcion incorrecta")

#Saldo
saldo = int(input("Tienes en total "))
