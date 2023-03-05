import os
import sys

# Obtenemos la ruta completa del archivo en ejecución
ruta_completa = os.path.abspath(sys.argv[0])

# Imprimimos la ruta completa
print("La ruta completa del archivo en ejecución es:", ruta_completa)