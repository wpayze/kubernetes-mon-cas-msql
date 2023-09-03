from cassandra.cluster import Cluster
from uuid import uuid1  
import random
import time
import traceback

cluster = Cluster(['cassandra-service']) 
keyspace = "cassandra_vehicles"

try:
    print("Intentando conectar a la base de datos...")
    session = cluster.connect(keyspace)
    print("Conectado a la base de datos.")

    start_time = time.time()
    batch_start_time = start_time
    total_elapsed_time = 0

    print("Insertando registros...")

    colors = ['red', 'blue', 'green', 'yellow', 'black', 'white', 'gray', 'silver', 'gold']
    insert_query = "INSERT INTO vehicles (vehicle_ID, model_id, year, color) VALUES (?, ?, ?, ?)"

    prepared = session.prepare(insert_query)

    for i in range(100000):
        vehicle_ID = str(uuid1())
        model_id = "7d866065-8287-42fd-b7a2-f9d436c954c6"
        year = random.randint(1990, 2023)
        color = random.choice(colors)

        session.execute(prepared, (vehicle_ID, model_id, year, color))

        if (i + 1) % 1000 == 0:
            batch_end_time = time.time()
            batch_elapsed_time = batch_end_time - batch_start_time
            total_elapsed_time += batch_elapsed_time

            print(f"{i + 1} registros insertados.")
            print(f"Tiempo transcurrido para estos 1,000 registros: {batch_elapsed_time:.6f} segundos")
            print(f"Rendimiento: {1000 / batch_elapsed_time:.2f} registros/segundo")
            print(f"Rendimiento promedio general: {(i + 1) / total_elapsed_time:.2f} registros/segundo")

            batch_start_time = batch_end_time

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo transcurrido total: {elapsed_time:.6f} segundos")

except Exception as err:
    print(f"Error al conectar o insertar en la base de datos: {err}")
    print("Información adicional:")
    print(traceback.format_exc())

finally:
    cluster.shutdown()
