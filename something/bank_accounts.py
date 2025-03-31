class Balance_Exception(Exception):
    pass

class BankAccount:
    def __init__(self, initial_amount, account_name):
        self.balance = initial_amount
        self.name = account_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balace = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDepostit complete.")
        self.get_balance()

    def can_withdraw(self, amount):
        if self.balance < amount:
            raise Balance_Exception(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
    
    def withdraw(self, amount):
        try:
            self.can_withdraw(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.get_balance()
        except Balance_Exception as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer_to(self, other, amount):
        try:
            print(f"\n************\n\nBeginning transfer...🚀")
            self.can_withdraw(amount)
            self.withdraw(amount)
            other.deposit(amount)
            print(f"\nTransfer Complete! ✅\n\n************")
        except Balance_Exception as error:
            print(f"\nTransfer interrupted. ❌ {error}")