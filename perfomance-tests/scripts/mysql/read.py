import mysql.connector
import time
import traceback  # para imprimir la traza completa del error

# Configura la información de la conexión a la base de datos
db_config = {
    "host": "mysql-service",
    "user": "root",
    "password": "mysqlpass123",
    "database": "mysql_vehicles"
}

try:
    # Intenta conectar a la base de datos
    print("Intentando conectar a la base de datos...")
    db_connection = mysql.connector.connect(**db_config)
    print("Conectado a la base de datos.")

    # Verifica la conexión
    db_connection.ping(reconnect=True, attempts=3, delay=5)  # reintenta hasta 3 veces, con un retardo de 5 segundos
    print("La conexión está activa.")

    # Crea un cursor
    cursor = db_connection.cursor()

    # Realiza la consulta SELECT
    print("Realizando consulta SELECT...")
    start_time = time.time()
    cursor.execute("SELECT * from vehicles")
    end_time = time.time()

    # Obtiene los resultados y cuenta los registros devueltos
    results = cursor.fetchall()
    num_rows = len(results)

    # Muestra los resultados
    # print("Registros devueltos:")
    # for row in results:
    #     print(row)

    # Muestra el tiempo transcurrido y la cantidad de registros
    elapsed_time = end_time - start_time
    print(f"\nTiempo transcurrido: {elapsed_time:.6f} segundos")
    print(f"Registros devueltos: {num_rows}")

except mysql.connector.Error as err:
    print(f"Error al conectar o consultar la base de datos: {err}")
    print("Información adicional:")
    print(traceback.format_exc())  # imprime la traza completa del error

finally:
    # Cierra el cursor y la conexión a la base de datos
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'db_connection' in locals() and db_connection.is_connected():
        db_connection.close()
