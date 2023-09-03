import mysql.connector
import uuid
import random
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
    batch_start_time = start_time 
    total_elapsed_time = 0

    print("Insertando registros...")
    
    colors = ['red', 'blue', 'green', 'yellow', 'black', 'white', 'gray', 'silver', 'gold']
    insert_query = "INSERT INTO vehicles (vehicle_ID, model_id, year, color) VALUES (%s, %s, %s, %s)"

    for i in range(100000):
        vehicle_ID = str(uuid.uuid4())
        model_id = "7d866065-8287-42fd-b7a2-f9d436c954c6"
        year = random.randint(1990, 2023)
        color = random.choice(colors)
        
        cursor.execute(insert_query, (vehicle_ID, model_id, year, color))

        if (i + 1) % 1000 == 0:
            batch_end_time = time.time()
            batch_elapsed_time = batch_end_time - batch_start_time
            total_elapsed_time += batch_elapsed_time
            
            print(f"{i + 1} registros insertados.")
            print(f"Tiempo transcurrido para estos 1,000 registros: {batch_elapsed_time:.6f} segundos")
            print(f"Rendimiento: {1000 / batch_elapsed_time:.2f} registros/segundo")
            print(f"Rendimiento promedio general: {(i + 1) / total_elapsed_time:.2f} registros/segundo")

            batch_start_time = batch_end_time 
    
    db_connection.commit()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo transcurrido total: {elapsed_time:.6f} segundos")

except mysql.connector.Error as err:
    print(f"Error al conectar o insertar en la base de datos: {err}")
    db_connection.rollback()

finally:
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
