"""
7. Chained Exception Handling / Custom Exceptions (Bonus)
Create your own custom exception class, e.g. class NegativeNumberError(Exception): ...
Write a function sqrt_positive(x) that:
If x is negative, raises NegativeNumberError with a message “Cannot compute square root of negative number.”
Otherwise returns math.sqrt(x)
In your main program, prompt the user for a number and call sqrt_positive. Use try / except to catch your custom exception and print its message.

"""
import math
class NegNUmError(Exception):

    pass
def sqrt_positive(num):
        if 0 > num:
              raise NegNUmError("Cannot compute square root of negative number.")
        else:
             return math.sqrt(num)     

if __name__ == '__main__':
      while True:
            try:
                 user_input = input("Enter a number to compute its square root (or 'quit' to exit): " )
                 if user_input.lower() == 'quit':
                       break
                 number = float(user_input)
                 result = sqrt_positive(number)
                 print(f"The square root of '{number}' is: {result}")

            except NegNUmError as e:
                  print(f"Error : {e}")
            except ValueError:
                  print("Error: invalid input. please enter valid number ")
            except Exception as e:
                  print(f"An unexpected Error occured: {e}")
                             


                 

             


                  


