"""
2. Using Python Standard Modules
Write a program that uses the math module to:
Compute square root of a number input by the user.
Compute the ceiling and floor values of a float number.
Also import random module to generate a random integer between 1 and 100 and print it.

"""
#Compute square root of a number input by the user
import math
import random
def modules_demo():
    try:
       num_sqrt = float(input("Enter non negative value compute it's square root : "))
       if num_sqrt < 0 :
           print("Error cannot compleat square root of a -ve number  ")
       else:
           root_sqrt= math.sqrt( num_sqrt )
           print(f"square root of {num_sqrt } is : {root_sqrt}")
    except ValueError:
        print("Invalid input of a square number.Please entered valid number  ")
           
              


# Compute the ceiling and floor values of a float number
def ceil_and_floor():
    while True:
        try:
           decimal_num = float(input("Enter a decimal number :"))
           ceil_val = math.ceil(decimal_num)
           floor_val = math.floor(decimal_num)

           print(f"Input number : {decimal_num}")
           print(f"ceiling value : {ceil_val}")
           print(f"floor value : {floor_val}")
           break
        except ValueError:
            print(f"Invalied input please enter valid decimal number. ")




#Generate Random Integer
def Random_integer():
    random_int = random.randint(1,100)
    print(f"Random integer between 1 and 100 is : {random_int}")

if __name__  == "__main__":
  modules_demo()
  ceil_and_floor()
  Random_integer()
  print("\nprogram finishid successully.")



    
