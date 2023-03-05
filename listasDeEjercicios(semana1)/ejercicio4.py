valor = input("Ingrese un valor: ")

if "." in valor:
    try:
        valor_float = float(valor)
        print("El valor ingresado es un float")
    except ValueError:
        print("El valor ingresado es una cadena")
else:
    try:
        valor_int = int(valor)
        print("El valor ingresado es un int")
    except ValueError:
        print("El valor ingresado es una cadena")
