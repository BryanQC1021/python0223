# Se le pide al usuario que ingrese los dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Se verifica si los dos números son iguales
if numero1 == numero2:
    print("Los dos números son iguales")

# Se verifica si los dos números son diferentes
elif numero1 != numero2:
# Se verifica si el primer número es mayor que el segundo
    if numero1 > numero2:
        print("El primer número es mayor que el segundo")
# Se verifica si el segundo número es mayor o igual que el primero
    if numero2 >= numero1:
        print("El segundo número es mayor o igual que el primero")
else: 
    print("Digite valores numéricos")