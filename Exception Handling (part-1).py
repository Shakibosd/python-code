# Python Bangla Tutorials 47 : Exception Handling (part-1)

'''
num1 = input("Enter a Number : ")
result = 20 / num1
print(result)
print("Done")
'''


'''
text = "Shakib"
print(text[5])
print("Done")
'''


'''try:
    list = [80,90,0,30,40,50]
    result = list[0] / list[2]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing By Zero Is Not Possible")
except IndexError:
    print("Index Error")
print("Successful")'''





try:
    list = [80,90,0,30,40,50]
    result = list[0] / list[8]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing By Zero Is Not Possible")
finally:
    print("Successful")






