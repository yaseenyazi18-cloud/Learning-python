"""
5. Special / Dunder Method
In your BankAccount or Person classes, overload some dunder methods, for example:
__str__ — returns a readable string when printing the object
__eq__ — to compare two objects (e.g. two Person objects equal if same name & age)
Demonstrate these methods in your main program (e.g. print(person1) or if person1 == person2:).

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"person(name={self.name} , age = {self.age})" 
    
    def __eq__(self, value):
        if isinstance(value, Person):
            return  self.name == value.name and  self.age == value.age
        return False
    
if __name__ == "__main__":    
  person1 = Person('Muhammed', 20)
  person2 = Person('Nadha', 23)
  person3 = Person('Muhammed', 20)
  person4 = Person('Muhammed', 25)



  print(person1) #__str__method
  print(person2) #__str__method
  if person1 == person2:
    print("person1 and person2 are equal.")
  else:
    print("person1 and person2 are not equal")

  if person1 == person3:
    print("person1 and person3 are equal.") 
  else:
    print("person1 and person3 are not equal.") 
  if person1 == person4:
    print("person1 and person4 are equal.")
  else:
    print("person1 and person4 are not equal") 
    
    print("---------------------------next method------------------------------------------")     

    print("Demonstrating __str__:")
    print(person1)
    print(person2)

    # Demonstrate __eq__
    print("\nDemonstrating __eq__:")
    print(f"Is person1 equal to person2? {person1 == person2}")
    print(f"Is person1 equal to person3? {person1 == person3}")
    print(f"Is person1 equal to person4? {person1 == person4}")

    # Example with a non-Person object for __eq__
    print(f"Is person1 equal to 'Muhammed'? {person1 == 'Muhammed'}")      
   


        
                