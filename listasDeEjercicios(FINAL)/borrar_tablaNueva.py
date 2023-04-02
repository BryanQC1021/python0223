import sqlite3

# Crear una conexión a la base de datos SQLite
conn = sqlite3.connect('datos.db')

# Crear un cursor
cursor = conn.cursor()

# Ejecutar la instrucción DROP TABLE para eliminar la tabla
cursor.execute("DROP TABLE tablaNueva")

# Confirmar los cambios
conn.commit()

# Cerrar el cursor y la conexión a la base de datos
cursor.close()
conn.close()