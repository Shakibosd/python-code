# Python Bangla Tutorials 45 : Reading a file

'''file = open("Student.txt","w")
print(file.writable())
file.close()'''



'''file = open("Student.txt","r+")
text = file.read()
print(text)
size = len(text)
print("Size = ",size)
file.close()'''



file = open("Student.txt","r+")
text = file.readline() [1]
print(text)
file.close()




file = open("Student.txt","r+")
for line in file:
    print(line)
file.close()

