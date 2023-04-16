# Python Bangla Tutorials 35 : Stack And Queue

books = []

books.append("Learn C")
books.append("Learn C++")
books.append("Learn Java")
print(books)

books.pop()
print("Npw The Top Book Is : ",books[-1])

books.pop()
print("Npw The Top Book Is : ",books[-1])

books.pop()
if not books:
   print("No Books Left")