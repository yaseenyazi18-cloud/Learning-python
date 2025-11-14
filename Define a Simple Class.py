"""
1. Define a Simple Class
Create a class Person with attributes: first_name, last_name, and age.
Include a method full_name() that returns the full name (first + " " + last).
Also include a method is_adult() that returns True if age ≥ 18, else False.
In your main program, create at least two Person objects with different data and print:
Their full names
Whether they are adults or not

"""
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def full_name(self):
         return self.first_name +" "+ self.last_name 
         
    def is_adult(self, age):
        if age > 18:
            return True
        else:
            return False     

person1 = Person('Muhammed', 'Yaseen A', 18)
person2 = Person('Ishan', 'kuttuo', 11)

print("Name: "+person1.full_name()+"\n Age: "+str(person1.age))
print("Name: "+person2.full_name()+"\n Age: "+str(person2.age))
