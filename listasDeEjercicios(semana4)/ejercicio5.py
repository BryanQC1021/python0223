import re

def validar_telefono(numero):
    patron = r'^9\d*$'
    if len(numero) == 9 and re.match(patron, numero):
        print("Número de teléfono válido.")
    else:
        print("Número de teléfono inválido.")