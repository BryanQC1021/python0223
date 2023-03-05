# Definimos un diccionario con las llaves y valores iniciales
curso = {"nombre de curso": "", "cantidad de alumnos": 0, "activo": False, "nombre de profesor": "", "max nota": 0, "alumnos": []}

# Pedimos al usuario que ingrese nuevos valores para el diccionario
curso["nombre de curso"] = input("Ingrese el nombre del curso: ")
curso["cantidad de alumnos"] = int(input("Ingrese la cantidad de alumnos: "))
curso["activo"] = bool(input("Ingrese si el curso está activo (True o False): "))
curso["nombre de profesor"] = input("Ingrese el nombre del profesor: ")
curso["max nota"] = float(input("Ingrese la nota máxima del curso: "))
curso["alumnos"] = input("Ingrese una lista de alumnos separados por comas: ").split(",")

# Imprimimos el diccionario
print("El diccionario es:", curso)
