class Calculadora:
    def __init__(self):
        # Indica que se ejecuto correctamente y que pase a la siguiente
        # instruccion
        pass

    # Metodo sumar que recibe 2 parametros: n1 y n2
    def sumar(self,n1,n2):
        # Imprime en la consola el texto Resultado y el valor de la suma de n1 y n2
        print(f"Resultado: {n1 + n2}")

    def restar(self,n1,n2): 
        # Indica que el metodo se genero correctamente y esta listo para implementar el codigo necesario
        pass

# Se crea una instancia de la clase Calculadora, es decir se crea un objeto
mi_calculadora = Calculadora()
# Invoca el metodo sumar del objeto
mi_calculadora.sumar(10,5)
