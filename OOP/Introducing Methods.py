# Python Bangla Tutorials 51 : Introducing Methods
print("\n")

class student:
    roll = ""
    gpa = ""

    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : ,{self.roll},  GPA :  {self.gpa}")


print("Student : Rahim Info:- ")
rahim = student()
rahim.set_value(101,3.45)
rahim.display()

print("\n")

print("Student : Rahim Info:- ")
karim = student()
karim.set_value(101,3.45)
karim.display()


print("\n \n \n \n \n")