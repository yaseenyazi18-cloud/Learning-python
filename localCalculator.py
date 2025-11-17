def add(num1,num2):
    return num1 + num2

def substraction(num1,num2):
    return num1 - num2
def divition(num1,num2):
    return num1 / num2

def multiplecation(num1,num2):
    return num1 * num2

while True:
    print("------------------------------------------")
    print("Calculator")
    print("------------------------------------------")
    print("1: Addition\n2: Substraction\n3: Divition\n4: Multiplecation\n5: Quit Calculator\n")
    options = input(">>Select your options:" )
    if options == '5':
       print("Exiting Program.....!")
       break
    if options in ('1' ,'2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if options == '1':
            print("Addition: ",add(num1,num2))
        elif options == '2':
            print("Subtraction: ",substraction(num1,num2))
        elif options == '3':
            print("Subtraction: ",divition(num1,num2))
        elif options == '4':
            print("Subtraction: ",multiplecation(num1,num2))
    else:
        print("ERROR: Your Entered number is wrong.please enter valid number")

