# Python Bangla Tutorials 35 : Stack And Queue

from collections import deque

bank = deque (["Anis","Karim","Bijoy"])
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print(bank)

bank.popleft()
print("No Person Left")
