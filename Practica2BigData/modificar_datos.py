from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["futbol"]
collection = db["jugadoras"]

def modificar_nombres():
    updates = [
        {"filter": {"nombre": "María"}, "update": {"$set": {"nombre": "MARÍA"}}},
        {"filter": {"nombre": "Lucía"}, "update": {"$set": {"nombre": "LUCÍA"}}}
    ]
    for update in updates:
        collection.update_one(update["filter"], update["update"])
    print("Nombres actualizados a mayúsculas.\n")

if __name__ == "__main__":
    modificar_nombres()
