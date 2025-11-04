"""
Search in a List
Task: Ask the user to enter 5 names and store them in a list. Ask the user to input a name to search
 for and print whether the name exists in the list or not using an if-else statement.

"""
name_list = []

print("enter five names: ")

for i in range(5) :
    store = (input("Enter name : "))
    name_list.append(store)
print(name_list)
search_key = (input("Enter a name for searching : "))  


if search_key in name_list :
    print(f"\nThe name '{search_key}' exists in the list.")
else :
    print(f"\nThe name '{search_key}' doesn't exists in the list.")    
