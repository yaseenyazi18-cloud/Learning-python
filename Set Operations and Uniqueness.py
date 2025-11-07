"""4. Set Operations and Uniqueness
Objective: Explore sets and their properties, such as uniqueness and set operations.
Tasks:



Check if an element exists in the set.
Convert a list with duplicates into a set to remove duplicates.
Expected Outcome: The program should demonstrate how sets automatically handle duplicates and support various set operations.
"""
#Create a set with duplicate elements and observe the result.
my_set = {2,33,4,2,33,6,87,6,56,6,7,77,"yazi",True,"yazi",33 }
print(f"Resualt is : {my_set}")

#Add and remove elements from the set.
my_set.add(False)
print(f"Add : {my_set}")
my_set.remove(33)
print(f"remove : {my_set}\n")

#Perform union, intersection, and difference operations with another set.
another_set = {2,3,4,2,3,7,66,55,98,True,False,True,(3,4,5)}

print(f"my set : {my_set}")
print(f"another_set : {another_set}\n")
result_union = my_set.union(another_set)
print(f"union method : {result_union}")
result_or = my_set | another_set
print(f"or |  : {result_or}\n")

result_intersection = my_set.intersection(another_set)
print(f"intersection result : {result_intersection}")
intersection_and = my_set & another_set
print(f"&  : {intersection_and}\n")

result_defference = my_set.difference(another_set)
print(f"defference result : {result_defference}")
intersection_myness = my_set - another_set
print(f"-  : {intersection_myness}\n")

#Check if an element exists in the set.
if  'yazi' in my_set:
    print("Element found in  my_set")
else :
    print("Element not found in my_set")    


#Convert a list with duplicates into a set to remove duplicates.
Value_list = [2,3.4,55,True,36,66.92,2,55,True]
print("New list :",Value_list)
new_set = set(Value_list)
print(new_set)