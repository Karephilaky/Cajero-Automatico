class Account:
    def _init_(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    def check_balance(self):
        print(f"Current balance: ${self.balance}")

class ATM:
    def _init_(self):
        self.accounts = {}

    def create_account(self, account_number, initial_deposit=0):
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[account_number] = Account(account_number, initial_deposit)
            print(f"Account {account_number} created with balance ${initial_deposit}")

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)

# Example usage
atm = ATM()
atm.create_account("12345", 100)
account = atm.get_account("12345")
if account:
    account.check_balance()
    account.deposit(50)
    account.withdraw(30)
    account.check_balance()