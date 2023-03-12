
def main():
    evento = obtEvent()
    validar(evento)
    procesar(evento)

def obtEvent():
    evento = input("Digite el nombre del evento: ")
    return evento

def validar(evento):
    eventos_validos = ['concierto', 'cumpleanios', 'fiesta']
    if evento.lower() not in eventos_validos:
        raise ValueError("El evento digitado no es válido.")

def procesar(evento):
    print(f"Evento {evento}...")

main()