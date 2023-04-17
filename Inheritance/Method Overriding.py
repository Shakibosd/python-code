# Python Bangla Tutorials 55 : Method Overriding

class phone:
    def __init__(self):
        print("I Am In Phone Class")


class samsung(phone):
    def __init__(self):
        super().__init__()
        print("I Am In Samsung Class")

s = samsung()