#Preguntar temperatura
temperatura = float(input("¿Qué temperatura hace? "))
estacion = input("¿En que estación estamos? ")

#Condiciones
if estacion == "Invierno" and temperatura<20:
    print("Deberías encender la calefacción")
elif estacion == "Verano" and temperatura>25:
    print("Deberías encender el aire acondicionado")
else:
    print("no es necesario encender ningún sistema de climatización")