def search(list,key):
    for i in range(len(list)):
        if list[i] == key:
            return 'Key element is found'
    return 'Element is not found'  


num = int(input("Enter list length:"))
list = [int(input())for i in range(num)]
print(list)
key = int(input('Enter the key element: '))
res = search(list,key)
print(res)
