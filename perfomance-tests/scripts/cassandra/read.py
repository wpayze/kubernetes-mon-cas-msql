from cassandra.cluster import Cluster
import time
import traceback

cluster = Cluster(["cassandra-service"])
keyspace = "cassandra_vehicles"

try:
    print("Intentando conectar a la base de datos...")
    session = cluster.connect(keyspace)
    print("Conectado a la base de datos.")

    print("Realizando consulta SELECT...")
    start_time = time.time()

    query = "SELECT * FROM vehicles"
    rows = session.execute(query)
    results = [row for row in rows]
    num_rows = len(results)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTiempo transcurrido: {elapsed_time:.6f} segundos")
    print(f"Registros devueltos: {num_rows}")

except Exception as err:
    print(f"Error al conectar o consultar la base de datos: {err}")
    print("Información adicional:")
    print(traceback.format_exc())

finally:
    cluster.shutdown()
