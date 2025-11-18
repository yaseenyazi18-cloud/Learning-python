To_Do_List = []

def addList():
    add_val = input("Enter a new task: ")
    To_Do_List.append(add_val)
    print(f"{add_val} added to the To_Do_List.")

def display():
    print("===================================")
    print(To_Do_List)
    print("===================================")
    for index,add_val in enumerate(To_Do_List,start=1):
        print(f"{index} - {add_val}")


def remomove():
    print(To_Do_List)
    remove_val = int(input("Enter remove value to To_Do_List: "))
    if 0<=remove_val < len(To_Do_List):
       To_Do_List.pop( remove_val)
    else:
        print("invalid number.")






while True:

     print("///////////////////////////////////////////////////////////")
     print("To Do List App")
     print("///////////////////////////////////////////////////////////")

     print("1: Add to list")
     print("2: Display list")
     print("3: remove list")
     print("4: Exist list")

     num = int(input("Select your option: "))
     if num == 1:
        addList()
     elif num == 2:
         display()
     elif num == 3:
         remomove()
     elif num == 4:
        print("Exit Program..")
        break
     else:
         print("Error: you entered number is invalid.Enter valid number.")