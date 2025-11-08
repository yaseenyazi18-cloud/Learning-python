

def div_samble(val1,val2):
     try:
         div = value1 / value2
         print(div)

     except ZeroDivisionError:
         print("Sorry ! You are dividing by zero ")



print("Enter 2 numbers ")
value1 = int(input("Enter first number : "))
value2 = int(input("Enter second number : "))
div_samble(value1,value2)    