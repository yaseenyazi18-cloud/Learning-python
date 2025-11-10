"""
Exception Handling: Multiple Exceptions
Write a program that prompts the user to input two numbers, but handle the following potential errors:
If user enters non-numeric input → catch ValueError
If dividing by zero → catch ZeroDivisionError
Use a try / except / else / finally structure. In finally, print a message like “Execution finished.”

"""
while True:
    try:
       print("--------Enter two numbers----------")
       val1 = float(input("Enter first numbers : "))
       val2 = float(input("Enter second number numbers : "))
       div = val1 / val2
    except ValueError:
       print("Error: Non-numeric input ditected.Please enter valid number.")
    except ZeroDivisionError:
       print("Error; cannot divided by zero")  
    else:
       print(f"The result of the division is {div}")
       break   
    finally:
       print("Execution finished")



