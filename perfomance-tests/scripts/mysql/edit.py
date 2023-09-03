import mysql.connector
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

    cursor.execute("SELECT vehicle_ID FROM vehicles LIMIT 100000")
    vehicle_ids = [row[0] for row in cursor.fetchall()]

    start_time = time.time()
    batch_start_time = start_time 
    total_elapsed_time = 0

    print("Actualizando registros...")

    colors = ['red', 'blue', 'green', 'yellow', 'black', 'white', 'gray', 'silver', 'gold']
    update_query = "UPDATE vehicles SET color = %s WHERE vehicle_ID = %s"

    for i, vehicle_ID in enumerate(vehicle_ids):
        color = random.choice(colors)
        
        cursor.execute(update_query, (color, vehicle_ID))

        if (i + 1) % 1000 == 0:
            batch_end_time = time.time()
            batch_elapsed_time = batch_end_time - batch_start_time
            total_elapsed_time += batch_elapsed_time
            
            print(f"{i + 1} registros actualizados.")
            print(f"Tiempo transcurrido para estos 1,000 registros: {batch_elapsed_time:.6f} segundos")
            print(f"Rendimiento: {1000 / batch_elapsed_time:.2f} registros/segundo")
            print(f"Rendimiento promedio general: {(i + 1) / total_elapsed_time:.2f} registros/segundo")

            batch_start_time = batch_end_time 
    
    db_connection.commit()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo transcurrido total: {elapsed_time:.6f} segundos")

except mysql.connector.Error as err:
    print(f"Error al conectar o actualizar en la base de datos: {err}")
    db_connection.rollback()

finally:
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
