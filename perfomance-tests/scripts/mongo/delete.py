from pymongo import MongoClient
import time

client = MongoClient('mongo-service', 27017)
db = client['mongo_vehicles']
collection = db['vehicles']

try:
    print("Eliminando registros...")
    start_time = time.time()

    cursor = collection.find({}, {'_id': 1}).limit(100000)
    for document in cursor:
        collection.delete_one({'_id': document['_id']})

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTiempo transcurrido: {elapsed_time:.6f} segundos")

except Exception as e:
    print("Error:", e)
