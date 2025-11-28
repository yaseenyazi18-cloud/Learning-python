
def Search(list,target):
    list2 = []
    flag = False
    for i in range(len(list)):
        if list[i] == target:
            flag = True
            list2.append(i)
           

    if flag == True:
        print("Key element is found at ")
        for i in list2:
           print(i)
    else:
        print("Element is not found ")        



list = [2,5,6,3,5,8]
print(list)
target = int(input("Enter search key: "))
Search(list,target)
