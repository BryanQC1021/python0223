# Solicitamos al usuario que ingrese los valores
valor1 = float(input("Ingrese el primer valor: "))
valor2 = float(input("Ingrese el segundo valor: "))
valor3 = float(input("Ingrese el tercer valor: "))

# Realizamos las operaciones matemáticas
suma = valor1 + valor2 + valor3
resta = valor1 - valor2 - valor3
multiplicacion = valor1 * valor2 * valor3
division = valor1 / valor2 / valor3
division_entera = valor1 // valor2 // valor3

# Imprimimos los resultados
print("La suma de los valores es:", suma)
print("La resta de los valores es:", resta)
print("La multiplicación de los valores es:", multiplicacion)
print("La división de los valores es:", division)
print("La división entera de los valores es:", division_entera)