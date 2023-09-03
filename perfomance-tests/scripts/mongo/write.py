from pymongo import MongoClient
import uuid
import random
import time

client = MongoClient('mongo-service', 27017)
db = client['mongo_vehicles']
collection = db['vehicles']

colors = ['red', 'blue', 'green', 'yellow', 'black', 'white', 'gray', 'silver', 'gold']
try:
    print("Insertando registros...")
    start_time = time.time()

    for i in range(100000):
        vehicle_ID = str(uuid.uuid4())
        model_id = "7d866065-8287-42fd-b7a2-f9d436c954c6"
        year = random.randint(1990, 2023)
        color = random.choice(colors)

        collection.insert_one({
            'vehicle_ID': vehicle_ID,
            'model_id': model_id,
            'year': year,
            'color': color
        })

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTiempo transcurrido: {elapsed_time:.6f} segundos")

except Exception as e:
    print("Error:", e)
