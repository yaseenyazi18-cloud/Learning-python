"""
4. Exception Handling: Division by Zero
Modify your divide(a, b) function in mymath.py so that it handles a scenario where b = 0. Use try / except to 
catch a ZeroDivisionError and return or print an error message like “Cannot divide by zero”.
In your main.py, prompt the user for two numbers and call this divide function. Test it with b = 0 to ensure your error handling works.


"""
from mymath import divide

num1 = float(input("Enter the numerator (num1): "))
num2 = float(input("Enter the denominator (num2): "))
result = divide(num1,num2)
print("result : ",result)