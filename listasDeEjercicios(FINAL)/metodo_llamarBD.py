import sqlite3


def leer_datos_de_db():
    # Crear una conexión a la base de datos SQLite
    conn = sqlite3.connect('datos.db')
    
    # Crear un objeto cursor
    cursor = conn.cursor()
    
    # Ejecutar una consulta SELECT para obtener todos los datos de la tabla 'tablaNueva'
    cursor.execute('SELECT * FROM tablaNueva')
    
    # Obtener todas las filas del resultado
    filas = cursor.fetchall()
    
    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()
    
    # Iterar sobre las filas y mostrar cada una
    for fila in filas:
        print(fila)
