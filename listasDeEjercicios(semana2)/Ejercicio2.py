
biblioteca = {
    "categorias": ["aventuras", "ciencia ficción", "cuentos de hadas", "gótica" ],
    "libros": {
        "El Código da Vinci": "Dan Brown",
        "1984": "George Orwell",
        "Harry Potter": "J.K. Rowling",
        "Lo que el viento se llevo": "Margaret Mitchell"
        
    },
    "prestamos": {},
    "usuarios": ["Pepe", "Jorge", "Martin", "Julio"]
}

print("Categorías de libros:")
for categoria in biblioteca["categorias"]:
    print(". " + categoria)

print("\nNombres de los libros y autores:")
for libro, autor in biblioteca["libros"].items():
    print(f"{libro} por {autor}")

# Cambiamos el estado de un libro a prestado
libro_prestado = "Caperucita Roja"
biblioteca["prestamos"][libro_prestado] = "Jorge"
print(f"\nSe ha prestado el libro {libro_prestado} a {biblioteca['prestamos'][libro_prestado]}.")

# Obtenemos la lista de usuarios de la biblioteca
print("\nUsuarios de la biblioteca:")
for usuario in biblioteca["usuarios"]:
    print("- " + usuario)