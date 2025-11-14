"""
2. Bank Account Class
Define a class BankAccount with:
Attributes: account_number, owner_name, balance (initially 0 or as argument)
Methods:
deposit(amount) — adds amount to balance
withdraw(amount) — subtracts amount if enough funds, else print “Insufficient funds”
display() — prints account details (account number, owner, balance)
In your main program:


Create an account for “Alice”, deposit some money, withdraw some, display info
Try to withdraw more than balance to test the “insufficient funds” behavior

"""
class BankAccount:
    def __init__(self,account_number, owner_name, balance=0 ):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("deposit Amount: ",amount) 

    def withdraw(self,amount):
        if self.balance > amount:
           self.balance -= amount
           print("Withdraw Amount: ",amount) 
        else:
            print("\n Insuffitient Amount") 
    
    def display(self):
        print("Owner Name: ",self.owner_name)
        print("Account Number: ",self.account_number)
        print("Account Balance:",self.balance)


bankacount = BankAccount(owner_name = 'Alice',account_number = 47553626)
bankacount.display()
bankacount.deposit(1000)
bankacount.withdraw(1500)





               