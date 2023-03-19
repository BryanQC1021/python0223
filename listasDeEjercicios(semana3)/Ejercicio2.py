from main import Item
from main import Catalogo

catalogo = Catalogo()

producto1 =Item("Llanta", "Llanta para automóvil", 1000)
catalogo.agregar_producto(producto1)

producto2 = Item("Batería", "Batería para automóvil", 2000)
catalogo.agregar_producto(producto2)

catalogo.mostrar_productos()