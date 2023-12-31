import mysql.connector
import time
import traceback  

db_config = {
    "host": "mysql-service",
    "user": "root",
    "password": "mysqlpass123",
    "database": "mysql_vehicles"
}

try:
    print("Intentando conectar a la base de datos...")
    db_connection = mysql.connector.connect(**db_config)
    print("Conectado a la base de datos.")

    db_connection.ping(reconnect=True, attempts=3, delay=5) 
    print("La conexión está activa.")

    cursor = db_connection.cursor()

    print("Realizando consulta SELECT...")
    start_time = time.time()
    cursor.execute("SELECT * from vehicles")
    
    results = cursor.fetchall()
    num_rows = len(results)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nTiempo transcurrido: {elapsed_time:.6f} segundos")
    print(f"Registros devueltos: {num_rows}")

except mysql.connector.Error as err:
    print(f"Error al conectar o consultar la base de datos: {err}")
    print("Información adicional:")
    print(traceback.format_exc()) 

finally:
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'db_connection' in locals() and db_connection.is_connected():
        db_connection.close()
