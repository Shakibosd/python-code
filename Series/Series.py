# Python Bangla Tutorials 27  Series

# 1 + 2 + 3 + ...... + n
n = int(input("Enter The Last Term : "))
sum = 0

for x in range(1, n+1, 1):
    sum = sum + x
print(sum)



# 2 + 4 + 6 + ...... + n
n = int(input("Enter The Last Term : "))
sum = 0

for x in range(2, n+1, 2):
    sum =  sum + x
print(sum)




# 1 + 3 + 5 + ...... + n
n = int(input("Enter The Last Term : "))
sum = 0

for x in range(1, n+1, 2):
    sum =  sum + x
print(sum)




# 4 + 8 + 12 + ...... + n
n = int(input("Enter The Last Term : "))
sum = 0

for x in range(4, n+1, 4):
    sum =  sum + x
print(sum)




# 1^2 + 2^2 + 3^2 + ...... + n^2
n = int(input("Enter The Last Term : "))
sum = 0

for x in range(1, n+1, 1):
    sum =  sum + x*x
print(sum)





# 1^3 + 2^3 + 3^3 + ...... + n^3
n = int(input("Enter The Last Term : "))
sum = 0

for x in range(1, n+1, 1):
    sum =  sum + x*x*x
print(sum)






# 2^2 + 4^2 + 6^2 + ...... + n^2
n = int(input("Enter The Last Term : "))
sum = 0

for x in range(2, n+1, 2):
    sum =  sum + x*x
print(sum)





# 2^3 + 4^3 + 6^3 + ...... + n^3
n = int(input("Enter The Last Term : "))
sum = 0

for x in range(2, n+1, 2):
    sum =  sum + x*x*x
print(sum)






# 1 + 1/2 + 1/3 + ...... + 1/n
n = int(input("Enter The Last Term : "))
sum = 0

for x in range(1, n+1, 1):
    sum =  sum + (1/x)
print(round(sum,2))








# 2 + 2/2 + 2/3 + ...... + 2/n
n = int(input("Enter The Last Term : "))
sum = 0

for x in range(2, n+1, 2):
    sum =  sum + (2/x)
print(round(sum,2))



