class Item:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        
    def __str__(self):
        return f"{self.nombre}: {self.descripcion} (${self.precio})"

class Catalogo:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

#---------------EJERCICIO 3---------------
def dividir(num1, num2):
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    else:
        return resultado
    
#---------------EJERCICIO 4y5--------------- 
import os

class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo
    
    def __str__(self):
        try:
            pais, lote, anio = self.codigo.split("-")
        except ValueError:
            print("El código no tiene el formato esperado.")
        else:
            print(f"Ruta del directorio de trabajo: {os.getcwd()}")
            return f"Producto: {self.nombre}\nCódigo: {self.codigo}\nPaís de origen: {pais}\nNúmero de lote: {lote}"
        finally:
            print("Proceso terminado")

#---------------EJERCICIO 6--------------- 
class Product:
    id=""
    nombre=""
    precio=""
    tipo=""
    stock=""
    release=""
    def __init__(self,id,nombre,precio,tipo,stock,release) -> None:
        self.id=id
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        self.stock=stock
        self.release=release
        pass
    def __str__(self) -> str:
        return f"el producto {self.nombre} de tipo {self.tipo} con id: {self.id}  de costo {self.precio} cuenta con {self.stock} stock"
    def updateStock(self,stock):
        self.stock=stock
    
class CarritoCompra:
    def __init__(self):
        self.listaProductos=[]
        self.precioTotal=0
    def agregarProducto(self,product:Product,cantidad=1):
        if self.validarStock(product):
            print("agregando producto")
            self.listaProductos.append(product)
            product.updateStock(product.stock-1)
        else:
            print("el producto no tienen stock")
         
    def quitarProducto(self, id_producto):
        for producto in self.listaProductos:
            if producto.id == int(id_producto):
                self.listaProductos.remove(producto)
                producto.updateStock(producto.stock + 1)
                print("Producto eliminado del carrito.")
                break
        else:
            print("No se encontró el producto en el carrito.")

    def calcularPrecio(self):
        for i in self.listaProductos:
            self.precioTotal+=i.precio
    def validarStock(self,product:Product):
        existe=False
        if product.stock>0:
            existe=True
        return existe
    def mostrarProductos(self):
        print(len(self.listaProductos))
        if len(self.listaProductos)>0:
            for i in self.listaProductos:
                print(i)
        else:
            print("carrito vacio")

