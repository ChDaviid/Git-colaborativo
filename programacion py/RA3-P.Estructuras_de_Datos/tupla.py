peliculas = [
    ("Shrek", 90),
    ("Toy Story", 81),
    ("Buscando a Nemo", 100)
]

#Indica qué tipo de estructura es peliculas y qué tipo de estructura representa cada película.
print(type(peliculas))
print(type(peliculas[0]))
print(type(peliculas[1]))
print(type(peliculas[2]))
print("--------------------------------")
#Recorre peliculas con un bucle y muestra el título y la duración de cada película.
for pelicula in peliculas:
    print(f"Título: {pelicula[0]}, Duración: {pelicula[1]} minutos")

print("--------------------------------")

# Añade la película ("Los Increíbles", 115) utilizando append().
peliculas.append(("Los Increíbles", 115))
print("--------------------------------")

# Vuelve a mostrar las películas para comprobar que se ha añadido.
for pelicula in peliculas:
    print(f"Título: {pelicula[0]}, Duración: {pelicula[1]} minutos")

print("--------------------------------")

# Intenta cambiar la duración de Shrek ejecutando esta instrucción: peliculas[0][1] = 95
# peliculas[0][1] = 95 error 

#7.la lista es un elemento que se puede modificar, pero la tupla es un elemento que no se puede modificar. Por eso, al intentar cambiar la duración de Shrek, se produce un error.