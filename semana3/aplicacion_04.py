class Numeros:

    def __init__(self):
        pass

    def numero_mayor(self,n1:int,n2:int,n3:int)->int:
        if n1 == n2 == n3:
            return n1
        elif n1 == n2:
            if n1 > n3:
                return n1
            else:
                return n3
        elif n2 == n3:
            if n2 > n1:
                return n2
            else:
                return n1
        elif n1 == n3:
            if n1 > n2:
                return n1
            else:
                return n2
        elif n1 > n2 and n1 > n3:
            return n1
        elif n2 > n1 and n2 > n3:
            return n2
        else:
            return n3

objeto = Numeros()        
while True:
    try:
        n1,n2,n3 = input("Ingresar 3 numeros (separados por ','): ").split(',')
        print(f"El numero mayor es: {objeto.numero_mayor(n1,n2,n3)}")
    except EOFError:
        print()
        break
