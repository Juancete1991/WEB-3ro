usuarios = {}



def guardar_informacion(nombre, contraseña):
    usuario = {
        "nombre": nombre,
        "contraseña": contraseña
    }

    usuarios[nombre] = usuario


def mostrar_informacion(usuarios):
    if not usuarios:
        print("No hay usuarios cargados todavia.")
    else:
        for nombre,contraseña in usuarios.items():
            print(f'Usuario: {nombre}, Constraseña: {contraseña['contraseña']}')


def login_usuario(usuarios):
    usuario_ingresado =input("Ingrese su nombre de usuario para ingresar:")
    contraseña_ingresada = input("Ingrese su contraseña para ingresar:")

    if usuario_ingresado in usuarios.keys():
        if usuarios[usuario_ingresado]['contraseña'] == contraseña_ingresada:
            print("Ha iniciado sesion!")
        else: print("Contraseña incorrecta.")

    else: print("Usuario no encontrado.")



while True:
    print("-----------MENU--------------")
    print("1. Registrar un nuevo usuario.")
    print("2 Iniciar Sesion.")
    print("3 Mostrar todos los usuarios.")
    print("4. Salir.")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        nombre = input("Ingrese nombre de usuario: ")
        contraseña = input("Ingrese contraseña: ")
        if nombre in usuarios:
            print("Ese nombre de usuario ya se encuentra registrado")
        else:
            guardar_informacion(nombre, contraseña)
            print("Usuario registrado correctamente.")
    elif opcion == "2":
        login_usuario(usuarios)
    elif opcion == "3":
        mostrar_informacion(usuarios)
    elif opcion == "4":
        print("Cerrando el programa...")
        break
    else:
        print("Opción inválida. Intente de nuevo.")

