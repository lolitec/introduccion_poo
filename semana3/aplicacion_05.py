"""
Ejemplo de uso de cadenas
"""

class Cadenas:

    def __init__(self, texto:str) -> None:
        self.texto = texto
        self.variable_local = "mmmmm"

    def longitud(self) -> None:
        print(len(self.texto))
        print(self.variable_local)

    def caracter(self, posicion:int) -> None:
        print(self.texto[posicion])

    def alcanceVariable(self, variable_local:str) -> None:
        print(self.texto)
        print(variable_local)

mi_objeto = Cadenas("Hola")
mi_objeto.longitud()
mi_objeto.caracter(2)

mi_objeto.alcanceVariable("adios")