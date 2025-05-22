class Numeros:

    def __init__(self):
        pass

    def numero_mayor(self,n1:int,n2:int,n3:int)->int:
        # Comprueba si todos son iguales
        if n1 == n2 == n3:
            return n1
        # Comprueba si el primero es igual al segundo
        elif n1 == n2:
            # Comprueba si el primero es mayor al tercero, si lo es regresa el primero de lo contrario regresa el tercero
            if n1 > n3:
                return n1
            else:
                return n3
        # Comprueba si el primero es igual al segundo
        elif n2 == n3:
            # Comprueba si el segundo es mayor al primero, si lo es regresa el segundo de lo contrario regresa el primero
            if n2 > n1:
                return n2
            else:
                return n1
         # Comprueba si el primero es igual al tercero
        elif n1 == n3:
            # Comprueba si el primero es mayor al segundo, si lo es regresa el primero de lo contrario regresa el segundo
            if n1 > n2:
                return n1
            else:
                return n2
        # Comprueba si el primero es mayor al segundo y tercero
        elif n1 > n2 and n1 > n3:
            return n1
        # Comprueba si el segundo es mayor al primero y tercero
        elif n2 > n1 and n2 > n3:
            return n2
        else:
            return n3

objeto = Numeros()       
# Bucle infinito para pedir un input al usuario y que lo pueda detener cuando quiera 
while True:
    try:
        # Se le pide al usuario ingresar 3 numeros separados por , para despues dividir el string en 3 variables n1,n2,n3
        n1,n2,n3 = input("Ingresar 3 numeros (separados por ','): ").strip().split(',')
        n1,n2,n3 = n1.strip(),n2.strip(),n3.strip()
        print(f"El numero mayor es: {objeto.numero_mayor(int(n1),int(n2),int(n3))}")
    # Esta excepcion permite al usuario salirse del programa al pulsar ctrl + d
    except EOFError:
        # Imprimir una linea vacia dado que la consola no lo hace al terminar el bucle
        print()
        # Termina el bucle
        break
    except ValueError:
        pass
