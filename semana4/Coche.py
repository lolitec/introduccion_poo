class Coche:
    def __init__(self,modelo:str,marca:str,anyo:int)->None:
        self.modelo = modelo
        self.marca = marca
        self.anyo = anyo
        self.velocidad = 0

    def acelerar(self,nueva_velocidad:float)->None:
        self.velocidad += nueva_velocidad

    def informacion(self)->None:
        print(f"Su auto es un: {self.marca} {self.modelo} {self.anyo} con una velocidad de {self.velocidad}km/hr")

marca = input("Ingrese la marca del coche: ")
modelo = input("Ingrese el modelo del coche: ")
while True:
    try:
        anyo = int(input("Ingrese el año del coche: "))
    except ValueError:
        print("Ingrese un valor numerico valido")
        pass
    else:
        break
mi_objeto = Coche(modelo,marca,anyo)

while True:
    try:
        aceleracion = float(input("Ingrese la nueva velocidad: "))
    except ValueError:
        print("Ingrese un valor numerico valido")
        pass
    else:
        break
mi_objeto.acelerar(aceleracion)
mi_objeto.informacion()
