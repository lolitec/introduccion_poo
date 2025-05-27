class CuentaBancaria:
    def __init__(self, numero_cuenta:int,titular:str) -> None:
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = 0

    def depositar (self,deposito:float) -> None:
        self.saldo += deposito

    def retirar(self,retiro:float) -> None:
        if retiro > self.saldo:
            print("El retiro no debe exceder el saldo disponible")
        else:
            self.saldo -= retiro

    def consultarSaldo(self):
        print(f"La cuenta {self.numero_cuenta} con el titular {self.titular} tiene un saldo de ${self.saldo}")

while True:
    try:
        numero_cuenta = int(input("Ingrese su numero de cuenta: "))
    except ValueError:
        pass
    else:
        break

titular = input("Ingresa el titular de la cuenta: ").title()
mi_objeto = CuentaBancaria(numero_cuenta,titular)
mi_objeto.consultarSaldo()

while True:
    operacion = input("Ingrese el número indicado según la operación que desea realizar:\n"
         "Si desea hacer un depósito ingrese 1\n"
         "Si desea hacer un retiro ingrese 2\n"
         "Para salir ingrese 3\n")

    match operacion:
        case "1":
            while True:
                try:
                    deposito = float(input("Ingrese la cantidad a depositar: "))
                    mi_objeto.depositar(deposito)
                    mi_objeto.consultarSaldo()
                except ValueError:
                    pass
                else:
                    break
        case "2":
            while True:
                try:
                    retiro = float(input("Ingrese la cantidad a retirar: "))
                    mi_objeto.retirar(retiro)
                    mi_objeto.consultarSaldo()
                except ValueError:
                    pass
                else:
                    break
        case "3":
            break
        case _:
            print("Opcion invalida")
