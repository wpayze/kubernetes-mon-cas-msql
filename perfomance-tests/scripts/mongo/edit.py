from pymongo import MongoClient
import random
import time

client = MongoClient('mongo-service', 27017)
db = client['mongo_vehicles']
collection = db['vehicles']

colors = ['red', 'blue', 'green', 'yellow', 'black', 'white', 'gray', 'silver', 'gold']
try:
    print("Actualizando registros...")
    start_time = time.time()

    cursor = collection.find({}, {'_id': 1}).limit(100000)
    for document in cursor:
        color = random.choice(colors)
        collection.update_one({'_id': document['_id']}, {'$set': {'color': color}})

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTiempo transcurrido: {elapsed_time:.6f} segundos")

except Exception as e:
    print("Error:", e)
