import psycopg2
from psycopg2 import Binary
import os
from psycopg2 import sql
from datetime import datetime


from urllib.parse import urlparse

parsed_url = urlparse(url)

#trying to connect to PGSQL cloud

 
NAME: parsed_url.path.strip('/')
USER: parsed_url.username
PASSWORD: parsed_url.password
HOST: parsed_url.hostname
PORT: parsed_url.port

try:
    # Conexión a la base de datos
    conn = psycopg2.connect(database=NAME, user=USER, password=PASSWORD, host=HOST , port=PORT)
    fecha_actual = datetime.now()

    # Lectura de la imagen
    nombreArchivo = "404.jpeg"
    ruta_archivo = os.getcwd() +  "/static/images/post/" + nombreArchivo 
    with open(ruta_archivo, 'rb',) as f:
        imagen_data = f.read()

    # Preparación de la consulta SQL
    cursor = conn.cursor()
    query =sql.SQL("INSERT INTO post (titulo, info, created_at, image ) VALUES (%s, %s, %s, %s)")
    data = ('prueba2', 'Infor acerca del post', fecha_actual , Binary(imagen_data))

    # Ejecución de la consulta
    cursor.execute(query, data)
    conn.commit()

    print("Consulta realizada correctamente")
except Error as e:
    print("Error", e)

finally:
# Cierre de la conexión
    cursor.close()
    conn.close()
    
    
