# Python Bangla Tutorials 60 : Magic methods

'''
class bike:
    def __init__(self,name,color):
        self.name = name
        self.color = color


    def __str__(self):
       return (f"Name = {self.name}, Color =  {self.color}")


    def display(self):
        print(f"Name = {self.name}, Color = {self.color}")

bike1 = bike("Yamaha R15","Blue")
bike2 = bike("Yamaha R15","Blue")
print(str(bike1))

'''




class bike:
    def __init__(self,name,color):
        self.name = name
        self.color = color


    def __eq__(self, other):
       return self.name == other.name and self.color == other.color


    def __str__(self):
       return (f"Name = {self.name}, Color =  {self.color}")


    def display(self):
        print(f"Name = {self.name}, Color = {self.color}")

bike1 = bike("Yamaha R15","Blue")
bike2 = bike("Yamaha R15","Blue")
print(bike1==bike2)

