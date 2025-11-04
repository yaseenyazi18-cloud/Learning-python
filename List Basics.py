#IT is a list of 5 fruits. Print the entire list and then print each fruit individually using a for loop

fivefruit = []

print("Enter your five favourite fruits names :")

i=1
while i < 6 :
    fruitname = input("Enter fruit name {i} : ")
    fivefruit.append(fruitname)
    i = i + 1

print(fivefruit)

for fruit in fivefruit :
    print(fruit)




