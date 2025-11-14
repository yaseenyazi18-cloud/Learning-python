"""
4. Student & Grades System
Define a class Student:
Attributes: name, roll_number, grades (a list of integers)
Methods:
add_grade(grade) — appends a grade
average_grade() — returns average of grades (use appropriate handling if list empty)
highest_grade() — returns the maximum grade
lowest_grade() — returns the minimum grade
In your program:
Create a student, add multiple grades, and then print average, max, min
Create at least two students and compare their average grades (print who is better)

"""
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades / len(self.grades))
        

    def highest_grade(self):
         if not self.grades:
            return 0
         return max(self.grades)

    def lowest_grade(self):
        if not self.grades:
            return 0
        return min(self.grades)   
            



        