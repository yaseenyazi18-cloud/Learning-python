def Search(list, target):
    low = 0
    heigh  = len(list)-1
    flag = False
    while low <= heigh:
        mid = (heigh + low) // 2
        if list[mid] == target:
            flag = True
            
        elif target > list[mid]:
            low = mid+1
        else:
            heigh = mid - 1     


    if flag == True:
        print('Element founded')
    else:
        print('Element not found')




list_len = int(input('Enter list length: \n'))
list = [int(input('Enter list element: ')) for i in range(list_len)]
list.sort()
print(list)
target = int(input('\nEnter search value: '))
Search(list,target)
