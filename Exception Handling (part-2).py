# Python Bangla Tutorials 48 : Exception Handling (part-2)

'''

try:
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number : "))
    result = num1 / num2
    print(result)

except (ValueError,ZeroDivisionError):
    print("You Are Enter Incorrect Input")
finally:
    print("Thanks !!!")

'''


def voter (age):
    if age < 18:
        raise ValueError("Invalid Voter")
    return  "You Are Allowed To Voter"

try:
    print(voter(19))
except ValueError as e:
    print(e)



