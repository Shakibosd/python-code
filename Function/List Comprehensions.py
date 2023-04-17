# Python Bangla Tutorials 42 : List Comprehensions

num = [1,2,3,4,5,6]
result = [x*x for x in num]
print("List = ",result)



num = [1,2,3,4,5,6]
result = [x for x in num if x%2==0]
print("List = ",result)