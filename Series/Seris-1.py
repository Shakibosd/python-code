# Python Bangla Tutorials 27  Series

# 1 X 2 X 3 X ...... X n
n = int(input("Enter The Last Term : "))
sum = 1

for x in range(1, n+1, 1):
    sum =  sum * x
print(sum)





# 2 X 4 X 6 X ...... X n
n = int(input("Enter The Last Term : "))
sum = 1

for x in range(2, n+1, 2):
    sum =  sum * x
print(sum)




# 4 X 8 X 12 X ...... X n
n = int(input("Enter The Last Term : "))
sum = 1

for x in range(4, n+1, 4):
    sum =  sum * x
print(sum)





# 1^2 X 2^2 X 3^3 X ...... X n^2
n = int(input("Enter The Last Term : "))
sum = 1

for x in range(1, n+1, 1):
    sum =  sum * x * x
print(sum)




# 2^2 X 4^2 X 6^3 X ...... X n^2
n = int(input("Enter The Last Term : "))
sum = 1

for x in range(2, n+1, 2):
    sum =  sum * x * x
print(sum)



# Factorial
num = int(input("Enter a number: "))

factorial = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")

else:
   for i in range(1, num + 1):
       factorial = factorial * i
   print("The factorial of",num,"is",factorial)






#prime number
lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)





#(gcd) & lcm
def find_gcd(a,b):
    gcd = 1
    for i in range(1,a+1):
        if a%i==0 and b%i==0:
           gcd = i
    return gcd

first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

print('HCF or GCD of %d and %d is %d' %(first, second, find_gcd(first, second)))

lcm = first * second / find_gcd(first, second)
print('LCM of %d and %d is %d' %(first, second, lcm))