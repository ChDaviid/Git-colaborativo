# pedir 10 numeros 
acumulador = 0
contador = 0
aprobadas = 0
for i in range(10):
    nota = float(input("Ingrese la nota: "))
    acumulador += nota
    contador += 1
    if nota >= 5:
        aprobadas += 1
        
#notas aprobadas
print("El total de notas aprobadas es: ", aprobadas)

#Media

print("El promedio es: ", acumulador / 10)