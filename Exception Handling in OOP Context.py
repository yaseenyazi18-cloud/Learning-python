"""
6. Exception Handling in OOP Context
In your BankAccount class’s withdraw method, raise a custom exception InsufficientFundsError if the amount
to withdraw is more than balance.Create that exception class. Use try / except in the main program to 
catch this exception and print a user-friendly message when withdrawal fails.

"""
class InsufficieantFundError(Exception):
    pass

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

      

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficieantFundError(f"Cannot withdraw {amount}. Current balance: {self.balance}")
        self.balance -= amount
        return self.balance

account = BankAccount(1000)   
try:
    account.withdraw(1500)
except InsufficieantFundError as e:
    print(f"Error withdrawal failed: {e}")
else:
    print(f"Withdrawal successful. New balance: {account.balance}")         
             



