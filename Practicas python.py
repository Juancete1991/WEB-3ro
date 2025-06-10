

#.......Try, Except, Else, Finally

# print("Decime unos numeracos en la siguiente opcion")

# try:    #se intenta ejecutar primero
#     num = int(input("decime dale: "))      
#     print(num)
# except Exception as e:
#     print("el error se llama ", e)
#     print("y el tipo de error es", type(e).__name__)
# except:   #se ejecuta si hay error
#     print("alguna cagada te mandaste")
# else:   #se ejecuta despues del try si no hay error
#     print("Bueno ahora sumale 2, restale 3 y metetelo en el culo")
# finally:  #si o si se ejecuta al terminar
#     print("eso es todo hayamos o no hecho la cuenta")

#.......POO

class Animal:
    def __init__(self, especie):
        self.especie = especie

    def describirEspecie(self):
        print(f"el animal es de la especie {self.especie}")

    def hacerRuido(self):
        raise NotImplementedError("Subclase debe implementar este metodo")  #raise es para que salte un error, en este caso si no implemento el metodo en la subclase, salta error
        


class Perro(Animal):
    #Atributo de clase
    patas = "cuatro"

    #Atributos de instancia
    def __init__(self, especie, nombre, edad, raza):     #este es el metodo constructor 
        super().__init__(especie)
        self.nombre = nombre
        self.__edad = edad
        self.raza = raza

    # def __init2__(self,nombre):
    #     super().__init__("perro")
    #     self.nombre = nombre        #no se pueden crear otras formas de constructor


    def getEdad(self):
        return self.__edad
    
    def setEdad(self,edad):
        self.__edad = edad

    def ladrar(self,nombre):   #este es un metodo de instancia normal
        print(f"el rompe pija de {nombre} esta ladrando")
        self.hacerRuido()

    @classmethod     #el decorador es obligatorio
    def verEspecie(cls):    #este es un metodo de clase, no necesita self, si no cls
        print(f"las patas del animal son {cls.patas}")
    
    @staticmethod
    def validarNombre(nombre):      #este es un metodo estatico, no necesita self ni cls, si no le pones el decorador staticmethod te salta error
        if len(nombre) > 0 and len(nombre) < 20:
            return True
        else:
            return False

    def hacerRuido(self):    #polimorfismo
        print("guau guau maderfaker")


class Gato(Animal):

    def __init__(self,nombre):
        super().__init__("gato")
        self.nombre = nombre


    def hacerRuido(self):
        print("miau miau moderfaker")  

perro1 = Perro("perroso","marco", 3, "oh noooo la polichia...casi")
perro1.ladrar(perro1.nombre)
print(Perro.verEspecie())
if Perro.validarNombre(perro1.nombre) is True:
    print(f"el perro se llama {perro1.nombre} y tiene {perro1.getEdad()} años y es de raza {perro1.raza}")

edadPerro = int(input("decime la edad del perro"))

perro1.setEdad(edadPerro)
print(f"ahora el perro tiene {perro1.getEdad()} años")

perro1.describirEspecie()

gato1 = Gato("miley")
gato1.hacerRuido()

animales = [Perro("Perro","Polo",8,"de la caye"),Perro("Perro","Norte",8,"idiota"),Gato("Titi")]

for animaletes in animales:
    print(animaletes.especie)
    print(f"{animaletes.nombre} esta rompiendo las bolainas, cuchaa cuchaa")
    animaletes.hacerRuido()

    