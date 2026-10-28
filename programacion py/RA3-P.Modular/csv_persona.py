import os
carpeta = os.path.dirname(os.path.abspath(__file__))
ruta = os.path.join(carpeta, "alumnos.csv")
with open(ruta, "r", encoding="utf-8") as fichero:
    datos = fichero.read()
filas = datos.splitlines()
suma_edades = 0
num_alumnos = 0
for fila in filas[1:]:
    if fila.strip() == "":
        continue
    campos = fila.split(";")
    if campos[2] == "DAW":
        print(campos[0])
    suma_edades = suma_edades + int(campos[1])
    num_alumnos = num_alumnos + 1
if num_alumnos > 0:
    media = suma_edades / num_alumnos
    print(f"Edad media: {media}")
else:
    print("No hay alumnos para calcular la media.")