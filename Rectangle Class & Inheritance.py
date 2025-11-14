"""
3. Rectangle Class & Inheritance
Create a base class Shape with a method area() (you can leave it to raise an error or return 0).
Create a subclass Rectangle(Shape) which:
Has attributes width and height
Overrides area() to return width * height
Create another subclass Square(Shape) which:
Takes just one side length
Its area() returns side²
In your program, instantiate a Rectangle and a Square, and print their areas.

"""
class Shape:
    def __init__(self, width, height=0):
        self.width = width
        self.height = height
        

class Rectangle(Shape):
    def area(self):
        return self.width * self.height


class Square(Shape):
    def area(self):
         return self.width**2 

value1 = float(input("Enter width : "))
value2 = float(input("Enter height: "))
rectangle = Rectangle(value1,value2)    
square = Square(value1)

print("Area of Rectangle: ",rectangle.area(),"sq")
print("Area of Square: ",square.area(),"sq")


