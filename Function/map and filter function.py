# Python Bangla Tutorials 41 : map and filter function

def square(x):
    return  x*x

num = [1,2,3,4,5]

result = list(map(square,num))
print("List = ",result)