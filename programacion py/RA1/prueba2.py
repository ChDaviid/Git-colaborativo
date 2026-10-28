texto = "Tres tristes tigres comen trigo en un trigal"
print(texto)
print(texto [0])
print(texto [19])
ultimo = len(texto)-1
print(texto[ultimo])
print(texto[0:4])
print(texto[2:5])
print(texto[0:4])


texto1 = "Hola \"Mundo\" de Python"
texto2 = "Lunes\tMartes\tMiercoles\tJueves"
texto3 = "Juan\nPepe\nDavid\nFelix\nVent\nNetanyahu"

print(texto1)
print(texto2)
print(texto3)




texto = "tres tristes tigres comían trigo en un trigal"
print(texto.upper())
print(texto.capitalize())
print(texto.title())
print(texto.count("t"))
print(len(texto))

subcadena = "tigres"
print(texto.index(subcadena))



nombre = input("¿Cómo de llamas? ")
edad_str = input("¿Qué edad tienes? ")
edad = int(edad_str)
if edad>17:
    print("eres mayor de edad")
    print("ya puedes votar")

else:
    print("vete con netan")
    print("menol")

print("hasta pronto")