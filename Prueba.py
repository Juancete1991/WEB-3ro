""" print ("Hola Mundo")
conjunto1 = input("ingrese numeros separados por coma")
conjunto2 = input("ingrese numeros separados por coma")
conjunto1 = set(conjunto1.split(","))
conjunto2 = set(conjunto2.split(","))
print(conjunto1.intersection(conjunto2))
conjuntoFusionado = conjunto1.union(conjunto2)
print(conjuntoFusionado) """     #shift alt A , lo trasnforma en comentario


""" stock = {"manzanas":50 , "bananas":30, "peras" : 40}
print(stock.items())

producto = input("decime el nombre del producto")
cantidad = input("decime la cantidad del producto")

stock[producto] = cantidad
print(stock)

productoAmodificar = input("decime cual querrias modificar")
cant = input("decime cuanto hay")
stock[productoAmodificar] = cant
print(stock)  """        # pero de esta forma si te equivocas agrega un nuevo producto asi

'''--------------------------segun chatgpt---------------------------------'''

# Diccionario con el stock inicial
stock = {"manzanas": 50, "bananas": 30, "peras": 40}
print("Inventario actual:", stock)

# Agregar un nuevo producto
producto = input("Ingrese el nombre del nuevo producto: ").lower()
cantidad = int(input("Ingrese la cantidad: "))

if producto in stock:
    print("Ese producto ya existe. Si deseas modificarlo, usa la opción de actualización.")
else:
    stock[producto] = cantidad
    print("Producto agregado.")

print("Inventario actualizado:", stock)

# Modificar un producto existente
productoAmodificar = input("Ingrese el nombre del producto que quiere modificar: ").lower()

if productoAmodificar in stock:
    cant = int(input("Ingrese la nueva cantidad: "))
    stock[productoAmodificar] = cant
    print("Cantidad actualizada.")
else:
    print("Ese producto no existe en el inventario.")

print("Inventario final:", stock)


# Controladores de Flujo


a = 195
b = 30
c = 400
if a > b and c > a:
  print("Ambas condiciones son verdaderas")    #Fijarse que no es necesario en el if los () y que al final del if van los :

a = 5
b = 150
print("A") if a > b else print("B")  #tambien se puede escribir asi de feo











