#participantes
participantes = ["Ana", "Luis", "Marta", "Luis", "Pablo"]
#Veces que aparece Luis
print("Veces que aparece Luis: ", participantes.count("Luis"))
#Posición de Marta
print("Posición de Marta: ", participantes.index("Marta"))
#Añadir un nuevo participante
participantes.append("Sara")
print(participantes)
#añadir elena posicion 2
participantes.insert(2, "Elena")
print(participantes)

#Borrar a pablo
participantes.remove("Pablo")
print(participantes)

#Ordenar alfabéticamente
participantes.sort()
print(participantes)

#Invertir el orden
participantes.reverse()
print(participantes)

#Extraer ultimo participante y mostrarlo
ultimo_participante = participantes.pop()
print("Último participante extraído: ", ultimo_participante)

#Mostrar la lista final de participantes
print("Lista final de participantes: ", participantes)