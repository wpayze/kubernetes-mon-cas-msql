import mysql.connector
import time

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

    start_time = time.time()

    print("Eliminando registros...")
    cursor.execute("DELETE FROM vehicles LIMIT 100000")

    db_connection.commit()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo transcurrido: {elapsed_time:.6f} segundos")

except mysql.connector.Error as err:
    print(f"Error al conectar o eliminar en la base de datos: {err}")
    db_connection.rollback() 

finally:
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'db_connection' in locals() and db_connection.is_connected():
        db_connection.close()
