"""
List Operations (Optional Challenge)
Task: Create a list of 10 random integers between 1 and 50. Use a loop to:
Count how many numbers are greater than 25.
Replace all numbers less than 10 with 0.
Print the updated list.

"""
random_list = []
count = 0
while True :
    num = int(input("Enter number between 1 to 50 : "))
    if num >= 1 and num <= 50 :
       random_list.append(num)
       count = count + 1
    else :
        print("Entered wrong number ,please enter valid number")      
    if count >= 10 :
        break  
print (random_list )

updated_list=[]
for i in random_list:
    if i<10:
        print(0)
        updated_list.append(0)
    else:
        print(i)
        updated_list.append(i)    

print(f"New list : {updated_list}")