facturas = [
  {
    "numero": 1000,
    "fecha": "30-04-2019",
    "cliente": {
      "nif": "516667788A",
      "nombre": "Pepe Sánchez",
      "tlf": "61777888"
    },
    "detalle": [
      {
        "producto": "Impresora Láser",
        "precio": 85,
        "cantidad": 2
      },
      {
        "producto": "CPU",
        "precio": 480,
        "cantidad": 1
      },
      {
        "producto": "Disco duro portatil",
        "precio": 53,
        "cantidad": 2
      }
    ]
  },
  {
    "numero": 1001,
    "fecha": "01-05-2019",
    "cliente": {
      "nif": "61777888J",
      "nombre": "Juan López",
      "tlf": "677888999"
    },
    "detalle": [
      {
        "producto": "Impresora de tinta",
        "precio": 45,
        "cantidad": 3
      },
      {
        "producto": "Caja de 100 CDs",
        "precio": 12,
        "cantidad": 2
      },
      {
        "producto": "Disco duro portatil",
        "precio": 51,
        "cantidad": 1
      }
    ]
  }
]

print(facturas[0]["detalle"][1])
print("--------------------------")
print(facturas[0]["cliente"]["tlf"])
print("--------------------------")
print(facturas[1]["cliente"]["nombre"])
print("--------------------------")
#importe de la segunda linea
print(facturas[0]["detalle"][1]["precio"]*(facturas[0]["detalle"][1]["cantidad"]))
print("--------------------------")
print(facturas[1]["detalle"][0]["precio"]*(facturas[1]["detalle"][0]["cantidad"])
      +facturas[1]["detalle"][1]["precio"]*(facturas[1]["detalle"][1]["cantidad"])
      +facturas[1]["detalle"][2]["precio"]*(facturas[1]["detalle"][2]["cantidad"]))
print("---------------------------")
