datos = """nombre;edad;curso
Ana;20;Python
Carlos;22;Java
Lucía;19;Python
Pedro;22;DAM"""

filas = datos.splitlines()
print(filas)

fila = filas[4]
campos = fila.split(";")
print(campos)


for fila in filas:
    campos = fila.split(";")
    print(campos)


print("--------------------------------")


for fila in filas[1:5]:
    campos = fila.split(";")
    print(campos)

