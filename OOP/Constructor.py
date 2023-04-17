# Python Bangla Tutorials 52 : Constructor

print("\n")

class student:
    roll = ""
    gpa = ""

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : ,{self.roll},  GPA :  {self.gpa}")


print("Student : Rahim Info:- ")
rahim = student(101,3.67)
rahim.display()

print("\n \n \n \n \n")