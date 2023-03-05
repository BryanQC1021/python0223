valor = int(input("Ingrese un número: "))
suma = 0

for i in range(1, valor+1):
    suma += i

print("La suma de los números hasta", valor, "es:", suma)