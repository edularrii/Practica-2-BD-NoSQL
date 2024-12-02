from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["futbol"]
collection = db["jugadoras"]

# Funciones de medición de tiempo
def tiempo_consulta_start_year():
    resultado = collection.find({"start_year": {"$gt": 2020}}).explain()
    tiempo = resultado['executionStats']['executionTimeMillis']
    documentos_examinados = resultado['executionStats']['totalDocsExamined']
    return tiempo, documentos_examinados

def tiempo_consulta_manchester():
    resultado = collection.find({"equipo.nombre": {"$regex": "^Manchester", "$options": "i"}}).explain()
    tiempo = resultado['executionStats']['executionTimeMillis']
    documentos_examinados = resultado['executionStats']['totalDocsExamined']
    return tiempo, documentos_examinados

def tiempo_consulta_por_pais(pais):
    resultado = collection.find({"equipo.pais": pais}).explain()
    tiempo = resultado['executionStats']['executionTimeMillis']
    documentos_examinados = resultado['executionStats']['totalDocsExamined']
    return tiempo, documentos_examinados

def crear_indices():
    collection.create_index([("start_year", 1)])
    collection.create_index([("equipo.nombre", 1)])
    collection.create_index([("equipo.pais", 1)])

if __name__ == "__main__":
    print("Medición sin índices:")
    tiempo1, docs1 = tiempo_consulta_start_year()
    print(f"Consulta start_year > 2020: {tiempo1} ms, {docs1} documentos examinados")
    
    tiempo2, docs2 = tiempo_consulta_manchester()
    print(f"Consulta equipos 'Manchester': {tiempo2} ms, {docs2} documentos examinados")
    
    tiempo3, docs3 = tiempo_consulta_por_pais("España")
    print(f"Consulta jugadoras en España: {tiempo3} ms, {docs3} documentos examinados")
    
    print("\nCreando índices...")
    crear_indices()
    print("Índices creados.\n")
    
    print("Medición con índices:")
    tiempo1_idx, docs1_idx = tiempo_consulta_start_year()
    print(f"Consulta start_year > 2020: {tiempo1_idx} ms, {docs1_idx} documentos examinados")
    
    tiempo2_idx, docs2_idx = tiempo_consulta_manchester()
    print(f"Consulta equipos 'Manchester': {tiempo2_idx} ms, {docs2_idx} documentos examinados")
    
    tiempo3_idx, docs3_idx = tiempo_consulta_por_pais("España")
    print(f"Consulta jugadoras en España: {tiempo3_idx} ms, {docs3_idx} documentos examinados")
