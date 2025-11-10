"""








4. Exception Handling: Division by Zero
Modify your divide(a, b) function in mymath.py so that it handles a scenario where b = 0. Use try / except to catch a ZeroDivisionError and return or print an error message like “Cannot divide by zero”.
In your main.py, prompt the user for two numbers and call this divide function. Test it with b = 0 to ensure your error handling works.



5. Exception Handling: Multiple Exceptions
Write a program that prompts the user to input two numbers, but handle the following potential errors:
If user enters non-numeric input → catch ValueError
If dividing by zero → catch ZeroDivisionError
Use a try / except / else / finally structure. In finally, print a message like “Execution finished.”



6. Reading a File with Exception Handling
Create a text file named data.txt and put some lines of text in it.
Write a Python program that attempts to open and read from data.txt. Use try / except to catch FileNotFoundError (if file doesn’t exist), and in the exception handler print a user-friendly message.
Also use finally to close the file or print “Done reading file” regardless of success/failure.



7. Chained Exception Handling / Custom Exceptions (Bonus)
Create your own custom exception class, e.g. class NegativeNumberError(Exception): ...
Write a function sqrt_positive(x) that:
If x is negative, raises NegativeNumberError with a message “Cannot compute square root of negative number.”
Otherwise returns math.sqrt(x)
In your main program, prompt the user for a number and call sqrt_positive. Use try / except to catch your custom exception and print its message.



"""
"""
1. Create and Use a Custom Module
Create a Python file named mymath.py that contains the following functions:
add(a, b) → returns sum of a and b
subtract(a, b) → returns a - b
multiply(a, b) → returns product
divide(a, b) → returns a / b
In another file (e.g. main.py), import your mymath module and use each of its functions, printing results.
"""
def add( num1 , num2 ):
    add = num1 + num2 
    return add
def subtract( num1 , num2 ):
    subtract = num1 - num2 
    return subtract
def multply( num1 , num2 ):
    multply = num1 * num2
    return multply
def divide( num1 , num2 ):
    try:
       divide = num1 / num2
       return divide
    except ZeroDivisionError:
      return "Error: value Cannot divide by zero.pleace enter new vlue."
 
      

    