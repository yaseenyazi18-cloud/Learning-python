"""
5. Even or Odd List Counter
Task: Ask the user to enter 10 numbers and store them in a list.
Count how many numbers are even and how many are odd.
Print both counts.

"""
values = []
odd = []
even = []
i = 0
while  i< 10 :
   num = int(input("Enter numbers : "))
   values.append(num)
   i = i + 1

for j in values :
    if j % 2 == 0 :
        even.append(j)
    else :
        odd.append(j)
print(odd)
print("number of odd is : ")
print(len(odd))
print(even)
print("number of even is : ")
print(len(even))
