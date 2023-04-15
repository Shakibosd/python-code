# Python Bangla Tutorials 34 : Set

'''

num1 = {34,56,78,90,90}
num2 = set([5,6,7,10])
num2.remove(10)
num2.add(9)

print(num1)
print(num2)
print(5 not in num2)
print(5 in num2)

'''



num1 = {34,56,78,90,90}
num2 = set([5,6,7,10, 34, 90])

print(num1 | num2)
print(num1 & num2)

