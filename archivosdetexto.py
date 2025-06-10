with open("archivo.txt", "w") as archivo:    #el with es para que no tengamos que cerrar el archivo manualmente, el "w" es para escribir, "r" para leer, "a" para agregar, "x" para crear, "t" para texto, "b" para binario, "U" para universal newline mode
    archivo.write("Hola, mundo!\n")
    archivo.write("Este es un archivo de texto.\n")



def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="UTF-8") as archivo:    #el encoding utf 8 es para que no de error con los caracteres especiales
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print(f"El archivo {nombre_archivo} no existe.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


leer_archivo("archivo.txt")

