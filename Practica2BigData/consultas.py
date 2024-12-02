from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["futbol"]
collection = db["jugadoras"]

# 2. Consultas

def consulta_start_year():
    print("Jugadoras con año de inicio mayor a 2020:\n")
    for jugadora in collection.find({"start_year": {"$gt": 2020}}):
        print(jugadora)
    print("\n\n")

def consulta_manchester():
    print("Jugadoras en equipos que empiezan con 'Manchester':\n")
    for jugadora in collection.find({"equipo.nombre": {"$regex": "^Manchester", "$options": "i"}}):
        print(jugadora)
    print("\n\n")

def consulta_por_pais(pais):
    print(f"Jugadoras que juegan en {pais}:\n")
    for jugadora in collection.find({"equipo.pais": pais}):
        print(jugadora)

# Ejecución de las funciones
if __name__ == "__main__":
    consulta_start_year()
    consulta_manchester()
    consulta_por_pais("España")