
while True:
    print("Menu")
    print("1. Dibujar un cuadrado")
    print("2. Muestre los numeros que son multiplos de 2 en la lista")
    print("3. Muestre a los mayores de edad de la lista")
    print("4. Salir")

    opc = input("Digite una opción: ")

    if opc == "1":
        tamanio = int(input("Digite el tamaño del cuadrado: "))

        for i in range(tamanio):
            for j in range(tamanio):
                if i == 0 or i == tamanio-1 or j == 0 or j == tamanio-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    
    elif opc == "2":
        Num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for numero in Num:
            if numero % 2 == 0:
                print(numero)
    
    elif opc == "3":
        personas = [("Bryan", 20), ("Alexandra", 27), ("Rocio", 15), ("Gabriel", 18), ("Renzo", 13)]

        for persona in personas:
            if persona[1] >= 18:
                print(persona[0])
    elif opc == "4":
        print("Adios")
        break
    else:
        print("Valor ingresado invalido")