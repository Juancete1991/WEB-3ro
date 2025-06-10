# num = 1
# tabla = [1,2,3,4,5,6,7,8,9,10]

# while num != 0:
#     num = int(input("Dame un número entero positivo (0 para salir): "))
    
#     if num == 0:
#         print("Terminado")
#         break
#     else:
#         print(f"Número ingresado: {num}, su tabla de multiplicar es:")
#         for numero in tabla:
#             print(f"{num} x {numero} = {numero * num}")

#----------------------------- Matchs, Whiles, For y listas

# num = 1

# listaSuper = ["tampones","manzana","tita","algo rico pa la gorda","lavandina","papel higienico","cacosa","mimosa"]
# listaCaract = ["gordos","grandes","muchas"]

# while num != 0:

#     num = int(input("Dame un numero y si queres una lista de super escribime 666 o 667 para sus caracteristicas tambien: "))

#     match num:
#         case 1:
#             print("te rompo el culo")
#         case 2:
#             print("yo te pongo la leche y vos el arroz")
#         case 3:
#             print("te la meto sin estres")
#         case 4:
#             print("te rompo el culo con el gato maraniato")
#         case 5:
#             print("por el culo te la inco")
#         case 6:
#             print("devuelta la quereis")
#         case 7:
#             print("haceme un pete")
#         case 8:
#             print("comete mi biscocho")
#         case 9:
#             print("agachate y conocelo, ahre")
#         case 0:
#             print("nos vemo en esaa")
#         case 666:
#             print("Esta es la lista de supermercado")
#             print(listaSuper)
#             for x in listaSuper:
#                 if x == "algo rico pa la gorda": continue
#                 print("xxx     " +  x)
#                 if x == "lavandina": break
#             else : 
#                 print("esa era la lista")
#         case 667:
#             for y in listaSuper:
#                 for x in listaCaract:
#                     print(y,x)
#         case _:
#             print(" de una cifra cara de pingo")

#------------------------------------------ Diccionarios



# diccionario = { "nombre":"Gordasa" , "esposo":"Juan" , "mascotas" : ["Polo","Marco","Miley","Listo ninguno mas"] , "edad" : 32 , "caca" : "liquida"}

# print(diccionario.items())
# diccionario.pop("caca")
# print(len(diccionario))

# print(diccionario.keys())
# print(diccionario.items())
# print(diccionario.values())

# for x in diccionario:
#     print(x)     #solo imprime los Keys no los Values
#     print(diccionario[x])   #aca solo los valores, sino podemos en vez de llamar a diccionario desps de in, ponerle el . values()

# for x , y in diccionario.items():   #tengo que iterar sobre los items uno a uno, no puede hacerlo asi nomas
#     print(x,y)
    
# dato = input("Que queres saber de mi memee ? nombre,esposo,mascotas o edad=     ")

# print(diccionario[dato])
# dato2 = input("otro mas?")
# print(diccionario.get(dato2))

# if "nombre" in diccionario:
#     print("el diccionario tiene la Key nombre")

# diccionario["esposo"] = "El mejor"

# diccionario.update({ "esposo" : "El mas mejor"})

# diccionario2 = { "nombre":"Gordo" , "esposa":"Gorda" , "mascotas" : ["Polo","Marco","Miley","Listo ninguno mas"] , "edad" : 34 , "caca" : "muy liquida"}

# familia = {"mujer" : diccionario , "varon" : diccionario2}

# print(familia["varon"]["nombre"])
# print(familia["mujer"]["nombre"])


#----------------------------- Actividad 10 guia 4


# print("Decime nombres rey, separados por un espacio")
# # while i < 5:
# #     nombres.append(input("Dime un nombre:"))
# #     i+=1

# nombres=input()
# lista = nombres.split()  #el Split convierte en Lista al String nombre, separando los valores segun el parametro, en este caso espacio ()

# print(f"esta es la lista {lista}")

# #lista = input("Ingresa nombres").split()  tambien asi

# for indice ,nombre in enumerate(lista):
#     print(f"Indice: {indice} Nombre: {nombre}")


#--------------------------- Actividad 11

# print("Decime varias palabras separadas por un espacio")
# palabras=input()
# palabras = palabras.lower()
# lista = palabras.split()
# salir=False

# for palabra in lista:
#     if palabra == "salir":
#         salir = True
#         break
#     elif palabra == "omitir":
#         continue
#     else:
#         print(palabra)

# if salir == False: print("nadie salio, se termino")
# else: print("se salio por el salir")


#----------------------------- Actividad 12

# productos = {}
# cantProd = 0

# while cantProd < 3:
#     producto=input("Nombre: ")
#     cantidad=int(input("Cantidad: "))

#     productos[producto] = cantidad

#     cantProd += 1

# print(productos.items())

# valorTotal = 0

# for x,y in productos.items():
#     print(x,y)
#     valorTotal += y

#     print(f"//  El saldo por ahora da {valorTotal}")

# print(f"////////El valor total da  {valorTotal}")



#------------------------------ Actividad Funciones 1) hacer

# def agregar_tarea(tareas,tarea):
#     tareas.append(tarea)


#------------------------------ Actividad Funciones 2)


def agregar_contacto(agenda, nombre, telefono, correo):   #usa un diccionario bidimensional
    agenda[nombre] = {"telefono":telefono, "correo":correo} #agenda es un diccionario, el nombre ingresado sera el key
    # y su value va a ser otro diccionario y va a ser telefono con su valor y correo con su valor


def buscar_contacto(agenda,criterio): #quiere buscar por nombre o numero de telefono.
    for nombre,info in agenda.items():
        if criterio in nombre or criterio == info["telefono"]:
            print(f"nombre: {nombre}")
            print(f"telefono: {info['telefono']}")
            print(f"correo: {info['correo']}")

agenda = {} #diccionario para contactos

while True:
    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Salir")
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        nombre = input("Ingresa nombre de contacto")
        telefono = input("Ingresa numero de contacto")
        correo = input("Ingresa correo de contacto")
        agregar_contacto(agenda,nombre,telefono,correo)
        print("contacto agregado.")
    elif opcion == "2":
        criterio = input("Ingresa el nombre o numero de telefono a buscar: ")
        buscar_contacto(agenda,criterio)
    elif opcion == "3":
        break
    



