class Calculadora:
    def __init__(self):
        print("Constructor")

    def sumar(self, numero1, numero2):
        return numero1 + numero2
    
mi_calculadora = Calculadora()
n1,n2 = input("Ingrese 2 números (separados por ','): ").split(",")
print(mi_calculadora.sumar(int(n1),int(n2)))
