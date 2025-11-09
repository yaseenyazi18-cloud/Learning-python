
#1. Basic Function Definition
#Task: Write a Python function named greet that takes a person's name as an argument and prints a greeting message.
def greet(name):
    print("Happt bithday to you : ",name)
    
greet("yaseen")    

"""2. Function with Return Value
Task: Create a function add_numbers that takes two numbers as parameters and returns their sum.
 Example Input:
 """
def add_number(num1,num2):
    sum = num1 + num2 
    return sum
print('Enter two number:')
values1 = int(input('Enter first number : '))
values2 = int(input('Enter second number : '))
sum = add_number(values1,values2)
print('return sum is : ',sum)

"""
3. Function with Default Parameters
Task: Define a function multiply that takes two numbers and returns their product. If the second number is not provided, it should default to 1.
"""
def defalt_num(num1,num2=1):
   product = num1 * num2
   return product

val1 = int(input('\nEnter first number : '))
val2 = int(input('Enter second number : '))
val = defalt_num(val1,val2)  
print("\nReturn Product value is : ",val) 

def defalt_val(num1,num2=1):
    product = num1 * num2
    return product

val = defalt_val(5)
print("Return Product value is : ",val)

"""
4. Function with Variable Number of Arguments
Task: Write a function concatenate_strings that takes any number of string arguments and returns a single string that is the concatenation of all the input strings.

"""
def  concatenate_strings(*argt):
    return "".join(argt)


valu = concatenate_strings('yaseen ,','nidhu',' its my family ','nadha ,','mom and ','dad'),
print(f"4 argumeants : {valu}")

"""
5. Function with Keyword Arguments
Task: Create a function student_info that accepts a student's name, age, and grade as keyword arguments and prints a formatted string displaying this information.

"""
def  student_info(name,age,grade):
    print(f"student name : {name},Age : {age},Grade : {grade}")

print("order key word :")
student_info( name="nadha", age=23 ,grade = "CMA" )
print("unorded key word :")
student_info(grade="3th", name="nidhu", age=9)

"""
7. Prime Number Checker Function
Task: Write a Python function is_prime(number) that takes an integer as input and returns True if print(result), otherwise returns False.
Then, ask the user to input a number and use this function to check if it is prime.
"""
import math
def is_prime(number):
    if number <= 1:
        print(f"Numbers less than or equal to 1 are not prime.")
        return False
    
    if number == 2 :
        print("2 is the only even prime number ")
        return True
    if number % 2 == 0:
        print("Even greater than 2 they are not prime number ")
        return False
    
    limit = int(math.sqrt(number))
    for i in range(3,limit + 1,2):
        if number % i == 0 :
            return False
    
    return True
    
    num = int(input("Enter a number : "))
result = is_prime(sum)
if result == True:
    print(f"{result} : The return number is prime number")
else:    
     print(f"{result} : The return number is not prime number")
