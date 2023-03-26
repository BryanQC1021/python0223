from datetime import datetime

class Registro:
    def __init__(self, filename):
        self.filename = filename
    
    def guardar_input(self, input_text):
        with open(self.filename, 'a') as f:
            current_time = datetime.now()
            f.write('{}-{}-{}\n'.format(current_time, self.filename, input_text))
    
    def mostrar_archivo(self):
        with open(self.filename, 'r') as f:
            print(f.read())