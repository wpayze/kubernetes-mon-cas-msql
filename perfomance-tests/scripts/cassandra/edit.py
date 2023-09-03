from cassandra.cluster import Cluster
import random
import time
import traceback

cluster = Cluster(['cassandra-service']) 
keyspace = "cassandra_vehicles"

try:
    print("Intentando conectar a la base de datos...")
    session = cluster.connect(keyspace)
    print("Conectado a la base de datos.")

    print("Recuperando IDs de vehículos...")

    vehicle_ids = []
    select_query = "SELECT vehicle_ID FROM vehicles LIMIT 100000"
    rows = session.execute(select_query)
    for row in rows:
        vehicle_ids.append(row.vehicle_ID)

    start_time = time.time()
    batch_start_time = start_time
    total_elapsed_time = 0

    print("Actualizando registros...")

    colors = ['red', 'blue', 'green', 'yellow', 'black', 'white', 'gray', 'silver', 'gold']
    update_query = "UPDATE vehicles SET color = ? WHERE vehicle_ID = ?"

    prepared = session.prepare(update_query)

    for i, vehicle_ID in enumerate(vehicle_ids):
        color = random.choice(colors)
        session.execute(prepared, (color, vehicle_ID))

        if (i + 1) % 1000 == 0:
            batch_end_time = time.time()
            batch_elapsed_time = batch_end_time - batch_start_time
            total_elapsed_time += batch_elapsed_time

            print(f"{i + 1} registros actualizados.")
            print(f"Tiempo transcurrido para estos 1,000 registros: {batch_elapsed_time:.6f} segundos")
            print(f"Rendimiento: {1000 / batch_elapsed_time:.2f} registros/segundo")
            print(f"Rendimiento promedio general: {(i + 1) / total_elapsed_time:.2f} registros/segundo")

            batch_start_time = batch_end_time

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo transcurrido total: {elapsed_time:.6f} segundos")

except Exception as err:
    print(f"Error al conectar o actualizar en la base de datos: {err}")
    print("Información adicional:")
    print(traceback.format_exc())

finally:
    cluster.shutdown()
