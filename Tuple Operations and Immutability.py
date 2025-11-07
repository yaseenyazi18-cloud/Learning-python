"""2. Tuple Operations and Immutability
Objective: Create and manipulate tuples to understand their properties and limitations.
Tasks:






Expected Outcome: The program should highlight the immutable nature of tuples and demonstrate basic tuple operations.
"""
#Create a tuple with mixed data types.
values=(22,3.5,True,[1,5],"NAME")
print(f"Tuple  : {values}")

#Access elements using indexing and slicing.
print(f"Element at index 3 {values[3]}")
print(f"Element at index 1  {values[1]}")
print(f"Element at slicing 2 to 4 {values[ 2 : 4]}")
print(f"Last index {values[-1]} ")

#Attempt to modify an element (to demonstrate immutability).
try :
    values[1]=5
    
except TypeError as e :
    print(f"Error :{e}")
    print(f"Tuple are immutable: individual element cannot be modified  ")
#tuple is immutable, if it contains a mutable object
# like a list, the contents of that mutable object *can* be changed.
print(f"before modify : {values}")
values[3].append(33)
print(f"after modify : {values}")

#Concatenate two tuples.
main_tuple = ("zero",21,3.8)
Concatenate_tuple = values + main_tuple
print(f"Concatenate tuple : {Concatenate_tuple}")

#Repeat a tuple multiple times.
repeat_tuple = values * 2
print(f"Repeated tuple{repeat_tuple}")
"""
#Convert a tuple to a list and back to a tuple.
tuple_list = []
for i in values :
    tuple_list.append(i)
print(f"Converted to list : "{tuple_list})

modify_tuple = tuple(tuple_list)
print(f"modify tuple : {modify_tuple}")
"""
print(f"current tuple : {values}")
list_value = list(values)
print(f"Tuple convert to list ; {list_value}") 
modify_tuple = tuple(list_value)
print(f"modify tuple : {modify_tuple}") 
