
import sys

def imprimir_argumentos():
    argumentos = sys.argv[1:]
    print("Los argumentos ingresados son:")
    for argumento in argumentos:
        print(argumento)

imprimir_argumentos()
