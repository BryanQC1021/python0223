
while True:
    print("Menu")
    print("1. Dibujar un cuadrado")
    print("2. Muestre los numeros que son multiplos de 2 en la lista")
    print("3. Muestre a los mayores de edad de la lista")
    print("4. Salir")

    opc = input("Digite una opción: ")

    if opc == "1":
        tamano = int(input("Digite el tamaño del cuadrado: "))

        for i in range(tamano):
            for j in range(tamano):
                if i == 0 or i == tamano-1 or j == 0 or j == tamano-1:
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
        personas = [("Jose", 20), ("Elizabeth", 27), ("Pepe", 15), ("Lisa", 18), ("Esteban", 13)]

        for persona in personas:
            if persona[1] >= 18:
                print(persona[0])
    elif opc == "4":
        print("Aios")
        break
    else:
        print("Valor ingresado invalido")