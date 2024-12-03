import os

index_global = 3


def registrar_producto(datos_producto):
    
    lista_de_productos.update({index_global+1:datos_producto})
    os.system("cls")
   
    

def mostrar_productos():
    os.system("cls")
    print("<----- Lista de Productos ------>")
    print(f"INDEX      |       Datos")
    for key in lista_de_productos:        
        print(f"{key}: {lista_de_productos[key]}")
    input("")



def actualizar_producto(key_producto):
    if key_producto in lista_de_productos:
        print(f"Seleccionaste el producto:{lista_de_productos[key_producto]}")
        nombre = input("Ingrese el nuevo nombre: ")
        precio = int(input("Ingrese el nuevo precio: "))
        stock = int(input("Ingrese el nuevo stock: "))
        categoria = input("Ingrese la nueva categoria: ")
        lista_de_productos[key_producto] = {"nombre":nombre,"precio":precio,"stock":stock,"categoria":categoria}
        mostrar_productos()
    else:
        print("Producto no encontrado")

lista_de_productos = {1:{"nombre":"Lampara","precio":3000, "stock":30, "categoria":"electro"},
                      2:{"nombre":"Radio","precio":2000, "stock":50, "categoria":"electro"},
                      3:{"nombre":"Mouse","precio":1900, "stock":10, "categoria":"electro" }}









#actualizar_producto(1)









opcion = ""

while opcion != "4":
    print("Bienvenido/a al sistema E-Mart")
    opcion = input(f'''Ingrese la opcion: 
                            1) Agregar producto 
                            2) Mostrar lista de productos 
                            3)Eliminar Producto 
                            4) Salir
                            Ingrese su opcion: ''')

    if opcion == "1":
        nombre = input("Ingrese el  nombre: ")
        precio = int(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock: "))
        categoria = input("Ingrese la categoria: ")
        datos_producto = {"nombre":nombre,"precio":precio,"stock":stock,"categoria":categoria}
        registrar_producto(datos_producto)
        index_global = index_global + 1
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "4":
        print("Gracias por visitarnos")
    else:
        print("OPCION NO ENCONTRADA")
