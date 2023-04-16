# Python Bangla Tutorials 38 : xargs and xxargs

'''
def student(*details):
    print(details)
student("Id = ",677392)
student("Name = ","Shakib")
student("gpa = ",3.10)

'''




def add(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num
    print("The Sum Is : ",sum)


add(20,10)
add(20,20,30)








