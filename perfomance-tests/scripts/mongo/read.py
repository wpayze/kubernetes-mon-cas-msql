from pymongo import MongoClient
import time

client = MongoClient('mongo-service', 27017)
db = client['mongo_vehicles']
collection = db['vehicles']

try:
    print("Realizando consulta...")
    start_time = time.time()
    
    cursor = collection.find()
    num_rows = cursor.count()
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTiempo transcurrido: {elapsed_time:.6f} segundos")
    print(f"Registros devueltos: {num_rows}")

except Exception as e:
    print("Error:", e)
