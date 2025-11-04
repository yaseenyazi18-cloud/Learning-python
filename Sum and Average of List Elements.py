
#2. Sum and Average of List Elements
#Task: Ask the user to enter 5 numbers and store them in a list. Calculate and print the sum and average of the numbers.
list = []
print("Enter five numbers : ")

i = 1
for i in range(5) :
    store = int(input())
    list.append(store)


total_sum = sum(list)
print("Enterd number are : "+str(list))    
print("The Sum of the numbers is: : "+str(total_sum))
avg = total_sum / len(list)
print("The Average of the numbers is: : "+str(avg))