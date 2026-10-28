# 4 intentos para ingresar la contraseña correcta
intentos = 0
max_intentos = 4
contraseña = "1234"
#pedir al usuario contraseña hasta que sea correcta
while True:
    intento = input("Ingrese su contraseña nuevamente: ")
    if intento == contraseña:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta. Intente nuevamente.")
        intentos += 1
    if intentos >= max_intentos:
        print("Has excedido el número máximo de intentos. Acceso denegado.")
        break
