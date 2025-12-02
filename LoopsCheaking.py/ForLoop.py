#1. Print Numbers 1 to 10 Task: Use a for loop to print the numbers from 1 to 10 (inclusive).
num = int(input("Enter star line length: "))

for i in range(1,num):
    print(i)

#2. Sum of a List Task: Calculate the sum of all numbers in the list [10, 20, 30, 40, 50]    
limit = int(input('Enter array limit: '))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(limit)]
sum = 0
for i in numbers:
    sum = sum + i
print("sum of list numbers: ",sum)    

#3. Calculate Squares Task: Print the square of each number from 1 to 5.

limit = int(input('enter limit number:'))
sq = 0
for i in range(1,limit):
    sq = i*i # i ** 2
    print(f"{i} square is: {sq}")
    
#4. Reverse a String Task: Reverse the string "Python" using a for loop (without using slice [::-1]).    

py = "python"
reversed_py = " "

p = "".join(reversed(py))
print(p)

for i in py:
    reversed_py =  i + reversed_py
print(reversed_py)    

#5. Find the Factorial (n!)Task: Calculate the factorial of 5 (5 * 4 * 3 * 2 * 1)

num = 5
factoriayal = 1
for i in range(1, num + 1):
    factoriayal = i * factoriayal
print(f"factoriayal of {num} is {factoriayal}")  

# #6. Count Vowels in a String Task: Count how many vowels (a, e, i, o, u) are in the string "Hello World".

vowels = "aeiouAEIOU"
text = "Hello World"
count = 0

for char in text:
   if char in vowels:
       count += 1
print(f"Count Vowels in a String is :{count}")   

#7. Find the Largest Number Task: Find the maximum value in [15, 82, 3, 19, 44] without using max()
num = [15, 82, 3, 19, 44, 90]
max_num = 0

for i in num:
    if i > max_num:
        max_num = i
print("Largest number; ",max_num)        


#8. Multiplication Table Task: Print a multiplication table for numbers 1 through 5.
 

for i in range(1,11):
    for j in range(1,11):
        print(f"{j}*{i} = {j*i} ")
    print("\n") 

#9. The Fibonacci Sequence Task: Print the first 10 numbers of the Fibonacci sequence (0, 1, 1, 2, 3, 5...).  

n = 10
a = 0
b = 1

for i in range(n - 2):
    #1 = 0 + 1
    c = a + b  
    print(f"{a} + {b} = {c}")
    a = b
    b = c

# 10. Construct a Pyramid Pattern Task: Print a star pyramid with 5 levels.
rows = 5
for i in range(1,rows + 1):
    print(" " * (rows - i), end=" ") 
    print("*" * (i * 2 - 1))

# 11.


