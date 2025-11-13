"""
4. Inheritance and Polymorphism
Create a base class Shape with:
Method area(self) — placeholder (e.g. raise NotImplementedError)
Method perimeter(self) — placeholder
Create derived classes:


Rectangle (inherits Shape) with width, height — override area() and perimeter()
Circle (inherits Shape) with radius — override area() and perimeter()
In main, create a Rectangle and Circle, and call their area() and perimeter() methods.

"""
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area method")
        
    def perimeter(self):
        raise NotImplementedError("Subclass must implement perimeter method")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
       
    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return self.width + self.height

class circle(Shape): 
#  Area: πr2         
#  Perimeter: 2πr 
#  math.pow(number, 2)
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius **2 

    def perimeter(self):
        return 2 * math.pi * self.radius 
    
rec_width = float(input("Enter rectangle width: ")) 
rec_height = float(input("Enter rectangle height: "))
radius = float(input("Enter Circle radius: "))  


rect = Rectangle(rec_width, rec_height)
circ = circle(radius)


print("Rectangle Area: ",rect.area())
print("Rectangle Perimeter: ",rect.perimeter())

print("\nCircle Area: ",circ.area())
print("Circle Perimeter:",circ.perimeter())
