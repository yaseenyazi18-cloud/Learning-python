"""
1. Create a Simple Class
Define a class Person with the following:
Attributes: name, age, gender
Method: display_info() — which prints the person's name, age, and gender.
In your main program, create two Person objects with different data and call their display_info() methods.

"""

class Person:
    def __init__(self, Name, Age, Gender):

        self.Name = Name 
        self.Age = Age
        self.Gender = Gender

    def display_info(self):
        print(f"Name : {self.Name}, Age : {self.Age}, Gender : {self.Gender}")    
    
person1 = Person('yaseen', 21 , 'Male')
person2 = Person ('nadha' , 23 , 'Female')

 
person1.display_info()
person2.display_info()
