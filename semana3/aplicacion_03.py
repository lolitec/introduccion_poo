'''
Ejemplo de parametros y tipos de datos
'''
class Calculadora:
    def __init__(self):
        pass

    def sumar(self,n1: int,n2: int):
        print(f"Resultado: {n1 + n2}")

    # Metodo dividir que recibe 2 parametros, divisor y dividendo
    def dividir(self,divisor: float,dividendo: float):
        try:
            # Imprime en la consola el texto Resultado y el valor de la division
            print(f"Resultado: {divisor/dividendo}")
            # Atrapa los errores posibles dentro del programa y los guarda en error
        except (ZeroDivisionError, TypeError) as error:
            # Imprime en la consola el texto Error y el mensaje de error almacenado en error
            print(f"Error: {error.args[0]}")
    
mi_calculadora = Calculadora()
mi_calculadora.sumar(10,5)
mi_calculadora.sumar("Hola ", "Adios")
mi_calculadora.dividir(10.0,2.0)
mi_calculadora.dividir("Hola",0.0)
