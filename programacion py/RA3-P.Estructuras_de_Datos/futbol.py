partidos = (    
 ("Real Madrid", "Barcelona", 2, 1),   
 ("Atlético de Madrid", "Sevilla", 0, 0),   
 ("Valencia", "Villarreal", 1, 3),   
 ("Athletic Club", "Real Sociedad", 2, 2),  
 ("Betis", "Celta", 3, 1),  
 ("Osasuna", "Getafe", 0, 1),   
 ("Espanyol", "Mallorca", 1, 0),   
 ("Alavés", "Rayo Vallecano", 1, 1),  
 ("Girona", "Las Palmas", 4, 2),   
 ("Leganés", "Valladolid", 0, 2),   
 ("Zaragoza", "Sporting", 2, 0),   
 ("Oviedo", "Racing de Santander", 1, 2),   
 ("Tenerife", "Eibar", 0, 0),   
 ("Málaga", "Granada", 3, 2)
)

def Equipo_local(partidos):
    return [partido[0] for partido in partidos]

def Equipo_visitante(partidos):
    return [partido[1] for partido in partidos]
def Goles_local(partidos):
    return [partido[2] for partido in partidos]

def Goles_visitante(partidos):
    return [partido[3] for partido in partidos]

def Obtener_resultados(partidos):
    resultados = []
    for partido in partidos:
        if partido[2] > partido[3]:
            resultados.append("Victoria local")
        elif partido[2] < partido[3]:
            resultados.append("Victoria visitante")
        else:
            resultados.append("Empate")
    return resultados

Equipo_local = Equipo_local(partidos)
Equipo_visitante = Equipo_visitante(partidos)
Goles_local = Goles_local(partidos)
Goles_visitante = Goles_visitante(partidos)
Resultados = Obtener_resultados(partidos)

for partido in partidos:
    print(f"{partido[0]} {partido[2]} - {partido[3]} {partido[1]}")
    print(f"Resultado: {Resultados[partidos.index(partido)]}")
    print("---------------------------------")