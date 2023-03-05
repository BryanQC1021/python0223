
# Definimos una lista con al menos 4 elementos que son tuplas de la forma (nombre, edad, dni)
personas = [("Juan", 25, "12345678"), ("María", 18, "87654321"), ("Pedro", 30, "23456789"), ("Laura", 16, "98765432")]

# Definimos una lista de DNIs
dnis = ["12345678", "23456789"]

# Definimos una lista vacía para almacenar las personas que cumplen las condiciones
personas_cumplen = []

# Iteramos sobre la lista de personas
for persona in personas:
    # Verificamos si la persona es mayor de edad y si su DNI está en la lista de DNIs
    if persona[1] >= 18 and persona[2] in dnis:
        # Si cumple las condiciones, agregamos su nombre a la lista de personas que cumplen
        personas_cumplen.append(persona[0])

# Imprimimos los nombres de las personas que cumplen las condiciones
print("Las personas que cumplen las condiciones son:", personas_cumplen)
