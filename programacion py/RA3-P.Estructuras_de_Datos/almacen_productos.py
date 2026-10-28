#Crear alamacén de productos
almacen_productos = []
#Mostrar menu repetidamente hasta que el usuario decida salir
while True:
    print("1. Añadir un nuevo producto")
    print("2. Listar todos los productos")
    print("3. Mostrar valor del almacen")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        nombre = input("Introduce el nombre del producto: ")
        stock = int(input("Introduce el stock del producto: "))
        precio = float(input("Introduce el precio del producto: "))

        producto = [nombre, stock, precio]
        almacen_productos.append(producto)
        print("---------------------------------------------------")

    elif opcion == "2":
        print("Productos en el almacén:")
        for producto in almacen_productos:
            print(producto)
            print("---------------------------------------------------")
    elif opcion == "3":
        valor_total = 0
        for producto in almacen_productos:
            valor_total += producto[1] * producto[2]
        print("Valor total del almacen:", valor_total)
        print("---------------------------------------------------")
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida")
