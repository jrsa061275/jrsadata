import pandas as pd
from funciones import leer_tabla_mysql, leer_json, leer_csv

# Llamamos a la función y guardamos los datos en un DataFrame
df_mysql = leer_tabla_mysql('localhost', 'root', '', 'db_ventas', 'llamadas_ventas')
#print(df_mysql.head())

df_json = leer_json('ventas_llamadas.json')
#print(df_json.head())

df_csv = leer_csv('llamadas_ventas.csv')
#print(df_csv.head())

#Definimos el orden final de columnas
columnas_final = ['id', 'fecha', 'duracion_min', 'duracion_min', 'agente', 'telefono_cliente', 'resultado']

#Reordenamos los DataFrames (por si acaso, así garantizas el orden, pero **no cambias los nombres**)
df_csv = df_csv[columnas_final]
df_mysql = df_mysql[columnas_final]
df_json = df_json[columnas_final]

#Unimos los tres DataFrames
df_unificado = pd.concat([ df_csv, df_mysql,  df_json], ignore_index=True)

#Guardamos el archivo CSV final
df_unificado.to_csv('resultado.csv', index=False)