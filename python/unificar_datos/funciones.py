# Importamos pandas para manejar los datos
# pip install pandas
import pandas as pd

# Importamos pymysql para la conexión con MySQL
#pip install pymysql
import pymysql


# Definimos una función para leer un archivo CSV
def leer_csv(ruta_csv):
    # Leemos el archivo CSV usando pandas
    df = pd.read_csv(ruta_csv)
    # Devolvemos el DataFrame con los datos
    return df



# Definimos una función para leer cualquier tabla de MySQL
def leer_tabla_mysql(host, user, password, database, tabla):
    # Creamos la conexión a la base de datos
    conexion = pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    
    # Escribimos la consulta SQL para traer todos los datos de la tabla
    consulta = f"SELECT * FROM {tabla};"
    
    # Ejecutamos la consulta y guardamos el resultado en un DataFrame
    df = pd.read_sql(consulta, conexion)
    
    # Cerramos la conexión
    conexion.close()
    
    # Devolvemos el DataFrame con los datos
    return df


def leer_json(ruta_json):
    # Leemos el archivo JSON usando pandas
    df = pd.read_json(ruta_json)
    # Devolvemos el DataFrame con los datos
    return df


