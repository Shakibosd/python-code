# Python Bangla Tutorials 57 : Types Of Inheritance

class A:
    def display(self):
        print("I Am Inside A Class")


class B(A):
    def display(self):
        print("I Am Inside B Class")


class C(B,A):
    pass

ob1 = C()
ob1.display()

























