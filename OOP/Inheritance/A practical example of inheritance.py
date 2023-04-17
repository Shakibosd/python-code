# Python Bangla Tutorials 56 : A practical example of inheritance

class shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("i am area method of shape class")

class tringle (shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Area of triangle : ",area)

class rectangle (shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of rectangle : ",area)

t1 = tringle(10,20)
t1.area()

r1 = rectangle(20,30)
r1.area()

