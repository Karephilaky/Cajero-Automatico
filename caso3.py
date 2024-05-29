class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    #Se unio la funcion deposit y withdraw en una sola
    def update_balance(self, amount, operation):
        if operation == "depositar":
            self.balance += amount
            print(f"Depositado ${amount}. Nuevo balance: ${self.balance}")
        elif operation == "retirar":
            if amount > self.balance:
                print("Fondos insuficientes.")
            else:
                self.balance -= amount
                print(f"Retirado ${amount}. Nuevo balance: ${self.balance}")

    def check_balance(self):
        print(f"Balance actual: ${self.balance}")

class ATM:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_deposit=0):
        if account_number in self.accounts:
            print("La cuenta ya existe.")
        else:
            self.accounts[account_number] = Account(account_number, initial_deposit)
            print(f"Cuenta {account_number} creada con balance ${initial_deposit}")

    def get_account(self, account_number):
        account = self.accounts.get(account_number)
        if not account:
            print("Cuenta no encontrada.")
        return account

# Función para manejar operaciones comunes
def handle_account_operation(atm, operation):
    account_number = input("Ingrese el número de cuenta: ")
    account = atm.get_account(account_number)
    if account:
        if operation == "check":
            account.check_balance()
        else:
            amount = float(input(f"Ingrese la cantidad a {operation}: "))
            account.update_balance(amount, operation)

# Ejemplo de uso con menú
def main():
    atm = ATM()

    while True:
        print("\nOpciones:")
        print("1. Crear cuenta")
        print("2. Verificar balance")
        print("3. Depositar")
        print("4. Retirar")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            account_number = input("Ingrese el número de cuenta: ")
            initial_deposit = float(input("Ingrese el depósito inicial: "))
            atm.create_account(account_number, initial_deposit)
        elif opcion == '2':
            handle_account_operation(atm, "check")
        elif opcion == '3':
            handle_account_operation(atm, "depositar")
        elif opcion == '4':
            handle_account_operation(atm, "retirar")
        elif opcion == '5':
            print("Gracias por usar el cajero automático. ¡Adiós!")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
