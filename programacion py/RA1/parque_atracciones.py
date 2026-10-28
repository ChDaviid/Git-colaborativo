#Preguntas para el parque
altura = int(input("¿Cuánto mides? "))
edad = int(input("¿Cuántos años tienes? "))
adulto = input("¿Vas acompañado? (S/N) ")

#Condiciones para subir Positivas
if altura>120 and edad>12:
    print("Puedes subir solo")
elif altura>120 and edad<12:
    print("Puedes subir pero solo acompañado" )
else:
    print("No puede subir a la atracción")