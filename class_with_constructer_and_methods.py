"""
2. Class with Constructor and Methods
Create a class BankAccount with:
Constructor __init__(self, owner_name, balance=0)
Method deposit(self, amount) — adds amount to balance
Method withdraw(self, amount) — subtracts amount if enough balance, else prints “Insufficient funds”
Method display_balance(self) — prints the current balance
In main, create an account and simulate deposits, withdrawals, and display the balance at each step.

"""
class BankAccount:
    def __init__(self,name):
        print("Acount holder name : ",name)
        self.balance = 0
        print("\n----------Welcome to Halal_bank----------\n")
    def deposite(self):
            deposite_amount = float(input("Enter amount to be deposite: "))
            self.balance += deposite_amount
            print("Amount deposited  :",deposite_amount)

    def withdraw(self):
          withdraw_amount = float(input("\nEnter amount to be withdrawn: "))
          if self.balance >= withdraw_amount:
                self.balance -= withdraw_amount
                print("Withdraw amount: ",withdraw_amount)
          else:
                print("\n Insufficient amount ")     
                
    def display_balance(self):
            print("\n Net valiable balance :",self.balance)


if __name__ == '__main__':
    val1 =  BankAccount('Muhammed yaseen A')

    val1.deposite()
    val1.withdraw()
    val1.display_balance()








        
        