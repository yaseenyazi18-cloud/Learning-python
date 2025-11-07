"""
Dictionary Operations and Key-Value Pairs
Objective: Understand how to work with dictionaries, focusing on key-value pairs.
Tasks:




Retrieve all keys, values, and items.

Use a loop to iterate over the dictionary and print each key-value pair.
Expected Outcome: The program should showcase the versatility of dictionaries in storing and accessing data.

"""
#Create a dictionary with at least five key-value pairs.
dic = {1:'yaseen',2:'nadha',3:'nidhu',4:'faseela',5:'shaheedha'}
my_dic = dict(name = 'yaseen',age = 21,std = 'degree',place = 'melattur',sub = 'b.com')
print(dic)
print(my_dic)

#Add a new key-value pair.
dic[6] = 'vappa'
my_dic["school"]='RMHSS'
print(f"\nDictionary after adding '6': {dic}")
print(f"Dictionary after adding 'school':{my_dic}")
#Remove a key-value pair 
del dic[1]
del my_dic['place']
print(f"\nRemove key-value pair: {dic}")
print(f"Remove key-value pair: {my_dic}")
#Remove a key-value pair by key.

removed_name = my_dic.pop('name')
print(f"\nDictionary after remove 'name' : {my_dic}")
print(f"Removed 'name' : {removed_name}" )

#Check if a key exists in the dictionary.

if 'degree' in my_dic :
    print(f"\nkey 'degree' exist in the dictionary : ")
else:
    print(f"key 'degree' not exist in the dict")

#Retrieve all keys, values, and items.
all_key = my_dic.keys()
all_values = my_dic.values()
all_items = my_dic.items()
print(f"\nall keys : {list(all_key)}")
print(f"All values : {list(all_values)}")
print(f"All items : {list(all_items)}")
#Update the value of an existing key.
dic[1] = 'mom'
print(f"\nUpdate value : {dic}")