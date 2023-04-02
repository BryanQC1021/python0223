from ejercicio2 import Sorteo
from ejercicio3 import get_tipo_cambio
from ejercicio4 import Registro
from ejercicio5 import validar_telefono

        #EJECUTANDO EJERCICIO 2
# Crear un objeto de la clase Sorteo
sorteo = Sorteo(50, 10)

# Sortear los números y mostrarlos
sorteo.sortear_numeros()
sorteo.mostrar_valores()

# Obtener un valor aleatorio de la lista
valor_aleatorio = sorteo.obtener_valor_aleatorio()
print("Valor aleatorio: {}".format(valor_aleatorio))


        #EJECUTANDO EJERCICIO 3
# Obtener los datos de la API de tipo de cambio
tipo_cambio = get_tipo_cambio()
print(tipo_cambio)


        #EJECUTANDO EJERCICIO 4
# Crear un objeto de la clase Registro
registro = Registro("registros.txt")

# Guardar un input en el archivo de registro
input_text = input("Ingrese un texto para guardar en el registro: ")
registro.guardar_input(input_text)

# Mostrar todo el archivo de registro
registro.mostrar_archivo()


        #EJECUTANDO EJERCICIO 5
# Validar un número de celular
numero = input("Ingrese un número de celular: ")
validar_telefono(numero)
