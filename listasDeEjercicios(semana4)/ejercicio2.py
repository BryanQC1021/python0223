import random

class Sorteo:
    def __init__(self, max_value, num_elements):
        self.values = []
        self.max_value = max_value
        self.num_elements = num_elements
    
    def sortear_numeros(self):
        for i in range(self.num_elements):
            self.values.append(random.randint(1, self.max_value))
    
    def mostrar_valores(self):
        print(self.values)
    
    def obtener_valor_aleatorio(self):
        return random.choice(self.values)
