#Logical Operators
#Write a Python program that checks if a number entered by the user is:


#Greater than 10 and less than 20.
num1 = int(input('Enter a number : '))

if num1 > 10 and num1 < 20 :
   print("This numbers is greater than 10 and less than 20\n")
else :
   print("This numbers are not greater than 10 and less than 20\n")
   

#Greater than 10 or less than 5.
num1 = int(input('Enter a number : '))

if num1 > 10 or num1 < 5 :
   print("This numbers is greater than 10 or less than 5\n")
else :
   print(+str(num1) +"\nThis numbers is not greater than 10 or less than 5\n")


#Not equal to 15.
num1 = int(input('\nEnter a number : '))

if not (num1 > 10 or num1 < 10) :
   print("This numbers is greater than 10 and less than 20\n")
else :
   print("This numbers is not greater than 10 and less than 20\n")
