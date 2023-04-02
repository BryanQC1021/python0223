import sqlite3

# Crear una conexión a la base de datos SQLite
conn = sqlite3.connect('datos.db')

# Crear un objeto cursor
cursor = conn.cursor()

# Crear una tabla 'usuarios' con las columnas 'id', 'nombre', 'apellido' y 'edad'
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                  (id INTEGER PRIMARY KEY,
                   nombre TEXT,
                   apellido TEXT,
                   edad INTEGER)''')

# Pedir al usuario que proporcione los valores para registrar una nueva fila
nombre = input("Ingrese el nombre del usuario: ")
apellido = input("Ingrese el apellido del usuario: ")
edad = int(input("Ingrese la edad del usuario: "))

# Insertar una nueva fila en la tabla 'usuarios' con los valores proporcionados por el usuario
cursor.execute('''INSERT INTO usuarios (nombre, apellido, edad) 
                  VALUES (?, ?, ?)''', (nombre, apellido, edad))

# Confirmar la transacción
conn.commit()

# Ejecutar una consulta SELECT para obtener todos los datos de la tabla 'usuarios'
cursor.execute('SELECT * FROM usuarios')

# Obtener todas las filas del resultado
filas = cursor.fetchall()

# Iterar sobre las filas y mostrar cada una
for fila in filas:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()

conn.close()