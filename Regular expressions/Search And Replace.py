# Python Bangla Tutorials 63 : Search And Replace

'''
import  re
pattern = r"Color"
text1 = "My Favorite  Color is red, i love red color"
text2 = re.sub(pattern,"Color",text1)
print(text2)
'''



import  re
pattern = r"Color"
text1 = "My Favorite  Color is red, i love red color"
text2 = re.sub(pattern,"Color",text1,count=2)
print(text2)