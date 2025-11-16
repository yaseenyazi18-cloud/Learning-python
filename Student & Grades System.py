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
        return sum(self.grades) / len(self.grades)
        

    def highest_grade(self):
         if not self.grades:
            return None
         return max(self.grades)

    def lowest_grade(self):
        if not self.grades:
            return None
        return min(self.grades)   
#creat student object            
student1 = Student('Muhammed Yasee A','11207')
student2 = Student('Nadha','12218')
#add grade for student1
student1.add_grade(30)
student1.add_grade(40)
student1.add_grade(70)
student1.add_grade(91)
#add grade for student2
student2.add_grade(90)
student2.add_grade(80)
student2.add_grade(70)
student2.add_grade(95)
#print average, max and min for the first student
print("---------student2",student1.name)
print("Average Grade of student1: ",student1.average_grade())
print("Max Grade of student1: ",student1.highest_grade())
print("Min Grade of student1: ",student1.lowest_grade())
print("-" * 25)

#print average, max and min for the second student
print("---------student2",student2.name)
print("Average Grade of student2: ",student2.average_grade())
print("Max Grade of student2: ",student2.highest_grade())
print("Min Grade of student2: ",student2.lowest_grade())
print("-" * 25)

#comparison average grade two students
print("____average grade comparison_____")
if student1.average_grade() > student2.average_grade():
    print(f'{student1.name} has a better average grade')
elif student1.average_grade() < student2.average_grade():
     print(f'{student2.name} has a better average grade')   
else:
    print(f"Both students are same average.")      







        