# Python Bangla Tutorials 30 : List as input from user

'''

n = input("Enter A Text Of Number : ")
sum = 0
list = n.split()

for num in list:
    sum = sum + int (num)
print("The Sum Is : ",sum)

'''


numOfDigit = 0
numOfLetter = 0
numOfWord = 0

text = input("Enter A Text Of Number : ")

for x in text:
    x = x.lower()
    if x>= 'a' and x<= 'z':
        numOfLetter = numOfLetter + 1
    elif x>= '0' and x<= '9':
        numOfDigit = numOfDigit + 1
    elif x== ' ':
        numOfWord = numOfWord + 1

print("Number Of Letter : ",numOfLetter)
print("Number Of Digit : ",numOfDigit)
print("Number Of Word : ",numOfWord)