from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sarah = BankAccount(2000, "Sarah")

Dave.get_balance()
Sarah.get_balance()

Sarah.deposit(500)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer_to(Sarah, 10000)
Dave.transfer_to(Sarah, 100)