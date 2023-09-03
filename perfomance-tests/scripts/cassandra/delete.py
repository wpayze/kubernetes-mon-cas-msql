from cassandra.cluster import Cluster
import time

cluster = Cluster(['cassandra-service'])
session = cluster.connect()

try:
    print("Intentando conectar a la base de datos...")
    session.execute("USE cassandra_vehicles")
    print("Conectado a la base de datos.")

    start_time = time.time()

    print("Eliminando registros...")
    rows = session.execute("SELECT vehicle_ID FROM vehicles LIMIT 100000")
    
    for row in rows:
        delete_query = "DELETE FROM vehicles WHERE vehicle_ID = %s"
        session.execute(delete_query, [row.vehicle_ID])

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo transcurrido: {elapsed_time:.6f} segundos")

except Exception as err:
    print(f"Error al conectar o eliminar en la base de datos: {err}")

finally:
    session.cluster.shutdown()
