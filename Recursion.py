# Python Bangla Tutorials 44 : Recursion

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


print("Factorial = ",fact(10))