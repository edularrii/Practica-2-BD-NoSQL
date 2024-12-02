from pymongo import MongoClient
import random

client = MongoClient("mongodb://localhost:27017/")
db = client["futbol"]
collection = db["jugadoras"]

nombres = ["María", "Lucía", "Carmen", "Laura", "Sofía", "Ana", "Paula", "Elena", "Isabel", "Andrea"]
apellidos = ["Gómez", "Fernández", "Martínez", "López", "García", "Rodríguez", "Pérez", "Sánchez", "Moreno", "Jiménez"]
equipos = [
    {"nombre": "Manchester United", "pais": "Reino Unido", "tipo": "club"},
    {"nombre": "Manchester City", "pais": "Reino Unido", "tipo": "club"},
    {"nombre": "Real Madrid", "pais": "España", "tipo": "club"},
    {"nombre": "Barcelona", "pais": "España", "tipo": "club"},
    {"nombre": "Paris Saint-Germain", "pais": "Francia", "tipo": "club"},
    {"nombre": "Olympique Lyon", "pais": "Francia", "tipo": "club"},
    {"nombre": "Juventus", "pais": "Italia", "tipo": "club"},
    {"nombre": "AC Milan", "pais": "Italia", "tipo": "club"},
    {"nombre": "Bayern Munich", "pais": "Alemania", "tipo": "club"},
    {"nombre": "Borussia Dortmund", "pais": "Alemania", "tipo": "club"},
]

grupos_sanguineos = ["O+", "A+", "B+", "AB+"]

def generar_datos():
    jugadoras = []
    for i in range(1, 101):
        jugadora = {
            "jugadora_id": str(i).zfill(3),
            "nombre": random.choice(nombres),
            "apellido": random.choice(apellidos),
            "edad": random.randint(18, 35),
            "equipo": random.choice(equipos),
            "start_year": random.randint(2015, 2024),
            "condicion_fisica": {
                "peso": random.uniform(50, 70),
                "altura": round(random.uniform(1.50, 1.80), 2),
                "grupo_sanguineo": random.choice(grupos_sanguineos),
            },
            "jugadas": {
                "posesion_porcentaje": random.randint(50, 90),
                "goles": random.randint(0, 30),
                "pases": random.randint(100, 500),
            },
        }
        jugadoras.append(jugadora)
    return jugadoras

jugadoras = generar_datos()
collection.insert_many(jugadoras)
print("Base de datos creada y 100 registros insertados.")
