ventas = [    
  {"producto": "Teclado", "precio": 25, "unidades": 2},    
  {"producto": "Ratón", "precio": 15, "unidades": 3},    
  {"producto": "Monitor", "precio": 180, "unidades": 1},  
  {"producto": "Teclado", "precio": 25, "unidades": 1},    
  {"producto": "Auriculares", "precio": 40, "unidades": 2},    
  {"producto": "Ratón", "precio": 15, "unidades": 4}
]

# Recorre la lista de ventas y construye un conjunto con los nombres.
conjunto = set()
for v in ventas:
    conjunto.add(v["producto"])

# Muestra el contenido del conjunto (los nombres)
print(conjunto)

# Muestra cuantos productos diferentes se han vendido
print(len(conjunto))

# Utiliza el conjunto para mostrar un resumen por producto que incluya
# el total de unidades vendidas y el importe total de sus ventas.
for p in conjunto:
    unidades = 0
    importe = 0
    for v in ventas:
        if (p==v["producto"]):
            uni=v["unidades"]
            pre=v["precio"]
            total=uni*pre
            unidades = unidades+uni
            importe = importe+total
    print(p, ":",unidades,"unidades", "-",importe, "€")