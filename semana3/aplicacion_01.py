class Calculadora:
    def __init__(self):
        print("Constructor")

    def sumar(self, numero1, numero2):
        print(f"Resultado: {numero1, numero2}")
    
mi_calculadora = Calculadora()
mi_calculadora.sumar(10,3)
