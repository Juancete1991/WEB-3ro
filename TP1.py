

usuarios = {}

def mostrar_nombres(usuarios):
    if not usuarios:
        print("No existen usuarios registrados.")
    else:
        print("Lista de usuarios:")
        for nombre in usuarios.keys():
            print(f"- {nombre}")


def mostrar_info(usuarios):
    if not usuarios:
        print("No existen usuarios registrados.")
    else:
        for nombre,contraseña in usuarios.items():
            print(f'Usuario: {nombre}, Constraseña: {contraseña['contraseña']}')


def login_usuario(usuarios):
    usuario_ingresado =input("Ingrese su nombre de usuario para ingresar:")
    contraseña_ingresada = input("Ingrese su contraseña para ingresar:")

    if usuario_ingresado in usuarios.keys():
        if usuarios[usuario_ingresado]['contraseña'] == contraseña_ingresada:
            print("Ha iniciado sesion de forma exitosa!")
        else: print("Contraseña incorrecta.")

    else: print("Usuario no encontrado.")

def guardar_informacion(nombre, contraseña):
    usuario = {
        "nombre": nombre,
        "contraseña": contraseña
    }
    usuarios[nombre] = usuario


while True:
    print()
    print("Bienvenido al sistema de registro e inicio de sesión.\n1")
    print("-----------------MENU-------------------")
    print()
    print("1. Registrar un nuevo usuario.")
    print("2. Iniciar Sesion.")
    print("3. Mostrar todos los usuarios.")
    print("4. Mostrar solo nombres de usuario.")
    print("5. Salir.")
    

    opcion = input("Seleccione una opción (1-5): \n")

    match opcion:
        case "1":
            nombre = input("Ingrese nombre de usuario: ")
            contraseña = input("Ingrese contraseña: ")
            if nombre in usuarios:
                print("Ese nombre de usuario ya se encuentra registrado")
            else:
                guardar_informacion(nombre, contraseña)
                print("Usuario registrado correctamente.")
        case "2":
            login_usuario(usuarios)
        case "3":
            mostrar_info(usuarios)
        case "4":
            mostrar_nombres(usuarios)
        case "5":
            print("Saliendo del sistema")
            break
        case _:
            print("Opción inválida. Por Favor intente de nuevo.")