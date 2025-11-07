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
i=0
while i<=4 :
    num = input(f"Enter a number : ")
    values.append(num)
    i=i+1
print(values)

#Add a new element at the end of the list.
values.append(input(f"Enter adding value : "))
print(values)

#Insert an element at a specific position.

values.insert(1,77)
print(f"insert : {values}")

#Remove an element by value and by index.
values.remove(input("Enter remove value :"))
print(values)

#Sort the list in ascending and descending order.
sort_values=[3,2,6,77,99,22,3,1,3,33,2]
print("Ascending:")
sort_values.sort()
print(sort_values)
print("DescenDing:")
sort_values.sort(reverse = True)

#Reverse the list. 
values.reverse()
print(f"reverse list : {values}")

 # find the index of a specific element
search = (input(f"Enter searching element :"))
index_value = values.index(search)
print(index_value )


   
