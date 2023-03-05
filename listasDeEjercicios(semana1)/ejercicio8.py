# Se guarda la contraseña en una variable
contraseña = input("Digite una contraseña: ")

# Se pide al usuario que ingrese una contraseña
entrada = input("Ingrese la contraseña: ")

# Se convierte la entrada del usuario y la contraseña en minúsculas
entrada_min = entrada.lower()
contraseña_min = contraseña.lower()

# Se verifica si la entrada coincide con la contraseña (en minúsculas)
if entrada_min == contraseña_min:
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")