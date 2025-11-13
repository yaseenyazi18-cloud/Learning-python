"""
3. Encapsulation (Private / Protected Attributes)
Modify the BankAccount class:
Make the balance attribute private (e.g. __balance)
Provide getter and setter methods: C and set_balance() with protections (e.g. disallow negative setting)
Try accessing __balance directly from outside (should not work), then use getter and setter to work with balance.

"""
class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance >= 0:
          self.__balance = initial_balance
        else:
            raise ValueError("Initial balance cannot be negative")  

    def get_balance(self):
        return self.__balance
        
    def set_balance(self, new_amount):
        if new_amount < 0:
            raise ValueError("balance cannot be negative")
        self.__balance += new_amount

ac = BankAccount(1000)

try:
    print(ac.__balance)
except AttributeError as e:
    print("Ditect access erroe:",e) 

print("Balance in getter:",ac.get_balance())

ac.set_balance(2000)
print("Balance in getter:",ac.get_balance())


try:
    ac.set_balance(-500)
except  ValueError as e:
    print("Setter protection error:", e)    















