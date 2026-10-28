#El programa contiene una lista con los dias de la semana en donde se va sumando de uno en uno las horas trabajadas hasta completar los dias de la semana, al llegar a los 5 dias se multiplica por 25 las horas totales lo que da el total del salario

semana =["lunes", "martes", "miercoles", "jueves", "viernes"]
total = 0 
i = 0
horas = 0
while i < 5:
    print("Horas trabajadas el dia", semana[i])
    horas = int(input())
    total = total + horas
    i +=1


salario = total * 25
print("El salario total es: ", salario)