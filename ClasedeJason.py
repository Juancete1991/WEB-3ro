import json  # Se importa el módulo json para trabajar con archivos JSON


# Lista de diccionarios con información de personas
datos = [
    {
        "nombre": "Leónidas",
        "edad": 30,
        "ciudad": "Santiago, Chile",
        "ocupacion": "Analista de Sistemas",
        "activo": False
    },
    {
        "nombre": "Ricardo",
        "edad": 25,
        "ciudad": "Mendoza, Argentina",
        "ocupacion": "Programador Python",
        "activo": True
    }
]


# Función para escribir los datos en un archivo JSON
def escribir_json(datos):
    try:
        # Se abre el archivo en modo escritura ("w")
        with open("datos.json", "w") as archivo:
            # Se vuelcan los datos al archivo con indentación para mejor lectura
            json.dump(datos, archivo, indent=4)  #sin el indent se ve todo en una linea, una cagada
    except Exception as e:
        # En caso de error, se muestra un mensaje
        print("Error al escribir datos en el archivo:", repr(e))


# Función para leer los datos desde el archivo JSON
def leer_json():
    try:
        # Se abre el archivo en modo lectura ("r")
        with open("datos.json", "r") as archivo:
            datos_json = json.load(archivo)  # Se cargan los datos del JSON
    except json.decoder.JSONDecodeError:
        # Error si el archivo JSON está dañado o mal formado
        print("Error al leer el archivo JSON, está corrupto")
    except FileNotFoundError:
        # Error si el archivo no se encuentra
        print("No se encontró el archivo")
    else:
        return datos_json  # Se devuelven los datos si todo salió bien


# Función principal del programa
def main():
    escribir_json(datos)  # Se escriben los datos en el archivo JSON
    lectura_json = leer_json()  # Se leen los datos del archivo JSON
    if not lectura_json:
        return  # Si no hay datos, se termina la ejecución
    print(lectura_json)  # Se imprimen los datos leídos


    # Ejemplo alternativo comentado para imprimir solo los nombres
    # for dato in lectura_json:
    #     print(dato["nombre"])


# Llamada a la función principal
main()
