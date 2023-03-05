import math

# Solicitamos al usuario que ingrese el radio
radio = float(input("Ingrese el radio: "))

# Calculamos el área del círculo
area_circulo = math.pi * radio**2

# Calculamos el área del triángulo
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area_triangulo = (base * altura) / 2

# Calculamos el área del cuadrado
lado = float(input("Ingrese el lado del cuadrado: "))
area_cuadrado = lado**2

# Imprimimos los resultados
print("El área del círculo es:", round(area_circulo, 2))
print("El área del triángulo es:", round(area_triangulo, 2))
print("El área del cuadrado es:", round(area_cuadrado, 2))
