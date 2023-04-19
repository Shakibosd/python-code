# Python Bangla Tutorials 62  Regular expressions

'''import re
pattern = r"Color"
if re.match(pattern,"Color Is Color, I Love Red Color"):
    print("Match")
else:
    print("Not Match")'''


'''import re
pattern = r"Color"
print(re.findall(pattern,"Red Is A Color, I Love Red Color"))'''


import  re
pattern = r"Color"
text = "My Favorite  Color is red"
match = re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())

















