def sample(num):
    if num < 0:
        print("Negative value")
    elif num == 0:
        print("Number is zero")
    else:
        print("number is positive")
def add_sample(val1,val2):
    sum = val1 + val2
    return sum

sample(int(input("enter the number : ")))
result = add_sample(3,6)
print("sum is :",result)