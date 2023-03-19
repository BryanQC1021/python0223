from main import CarritoCompra
from main import Product

message="""
    1)Agregar Producto
    2)Mostrar Productos
    3)Quitar Producto
    4)Mostrar Precio total
    5)Salir
"""
id=0
carrito=CarritoCompra()
while True:

    print(message)
    opcion=int(input("ingrese la opcion a realizar:"))
    if opcion==1:
        try:
            id=id+1
            name=input("ingrese el nombre del producto:")
            precio=float(input("ingrese el precio del producto:"))
            tipo=input("ingrese el tipo del producto:")
            stock=int(input("ingrese el stock del producto:"))
            release=int(input("ingrese el release del producto:"))
            px=Product(id,name,precio,tipo,stock,release)
            carrito.agregarProducto(px)
        except Exception as Error:
                print("sucedio un error")
        else:
            print("agregando en el menu")
    if opcion==2:
        carrito.mostrarProductos()
    if opcion==3:
        id_producto = input("Ingrese el ID del producto a quitar: ")
        carrito.quitarProducto(id_producto)
    if opcion==4:
        carrito.calcularPrecio()
        print(f"El precio total del carrito es: {carrito.precioTotal}")
    if opcion==5:
        break