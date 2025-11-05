"""
 List Operations and Manipulations
Objective: Develop a program that performs various operations on lists, including adding, removing, and modifying elements.
Tasks:
Create a list of 10 integers.
Add a new element at the end of the list.
Insert an element at a specific position.
Remove an element by value and by index.
Sort the list in ascending and descending order.
Reverse the list.
Find the index of a specific element.
Expected Outcome: The program should demonstrate the ability to manipulate lists effectively using various methods.

"""

values = []
i=1
while i<=10 :
    num = int(input("Enter a number : "))
    values.append(num)
    i=i+1
print(values)

#Add a new element at the end of the list.
values.append(int(input("Enter adding value : ")))
print(values)

#Insert an element at a specific position.
values.insert(1,77)
print(values)

#Remove an element by value and by index.
values.remove(0)
print(values)

#Sort the list in ascending and descending order.
values.sort
