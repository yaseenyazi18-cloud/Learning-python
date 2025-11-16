
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
 
      

    