import pandas as pd
import sqlite3
from metodo_llamarBD import leer_datos_de_db

# Carga de archivo CSV con pandas (1)
data = pd.read_csv('bdPrueba.csv')

# Operación sobre el archivo (por ejemplo, filtrado) (1.1)
data_filtrada = data[data['CANTIDAD'] >= 1000]
print(data_filtrada)

# Crear una conexión a la base de datos SQLite (2)
conn = sqlite3.connect('datos.db')
data_filtrada.to_sql('tablaNueva', conn, if_exists='replace', index=False)
conn.close()

print('##################################################################################')

#llamando al metodo (2.2)
leer_datos_de_db()