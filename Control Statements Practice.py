"""
Control Statements Practice
Task: Write a Python program that prints numbers from 1 to 20 but:
Skips numbers divisible by 3 using continue.
Stops the loop when a number greater than 15 is reached using break.

"""
for i in range(1,20,1) :
    if i % 3 == 0 :
        continue
    if i > 15 :
        break
    print(i)
       
       
       
