#Preguntar la edad
edad = float(input("¿Cuántos años tienes? "))
#Preguntar dia de la semana
dia_semana = "Lunes, Martes, Miercoles, Jueves, Viernes"
dia_finde = "Sábado, Domingo"

dia = input("¿Qué dia es? ")

if dia in dia_semana:
    print("El precio vale 15€")
    precio = 15
elif dia in dia_finde:
    print("El precio vale 20€")
    precio = 20

if edad<18:
        print("Tienes un descuento de 30%")
        precio = precio-precio*0.3


print ("precio", precio)



