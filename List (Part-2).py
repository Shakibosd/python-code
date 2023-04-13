# Python Bangla Tutorials 24 : List (Part-2)

subject = ["C","C++","Python","JavaScript","React","Java","PHP","Go","Jengo","C#","HTML","CSS","Bootstrap","R","Dart"]
print(len(subject))

subject.append("TOC")
print(subject)

subject.insert(2,"OS")
print(subject)

subject.remove("C++")
print(subject)



result = [52,14,58,54,57,5,2,4,93,87,12]
result.sort()
print(result)

result.reverse()
print(result)




sub = [52,14,58,54,57,5,2,4,93,87,12]
sub.pop()
print(sub)



sum = [52,14,58,54,57,5,2,4,93,87,12]
sum.clear()
print(sum)



div = [52,14,58,54,57,5,2,4]
div2 = div.copy()
print(div2)





pos = [52,14,58,54,57,5,2,4,93,87,12]
ind = pos.index(5)
print(ind)
ind = pos.index(2)
print(ind)




iub = [52,14,58,54,57,5,2,4,4,4,93,87,12]
iut = iub.count(4)
print(iut)