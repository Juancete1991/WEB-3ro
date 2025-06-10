import datetime


def agregarMerca():
    

    fecha = str(datetime.datetime.today())
    descripcion = input(f"Decime Descripcion:\n")
    cantidad = input(f"Decime Cantidad:\n")

    with open("registro.txt","a") as registro: #el "a" es para agregar al mismo archivo, si pongo "w" me sobreescribe el archivo
    
        registro.write(f"{descripcion}\n")   #el f me permite usar variables dentro de un string y el \n me permite hacer un salto de linea
        registro.write(f"{cantidad}\n")
        registro.write(f"{fecha}\n")


agregarMerca()