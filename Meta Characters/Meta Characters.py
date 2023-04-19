# Python Bangla Tutorials 64  Meta Characters

'''
import re

pattern = r"Colo..r"
if re.match(pattern,"Colobur"):
    print("Matched")
'''



'''
import re

pattern = r"^Colo..r$"
if re.match(pattern,"Colobur"):
    print("Matched")
'''



'''
import re

pattern = r"a*"
if re.match(pattern,"aolobur"):
    print("Matched")
'''


'''
import re

pattern = r"a+"
if re.match(pattern,"aolobur"):
    print("Matched")
'''



'''
import re

pattern = r"a+b"
if re.match(pattern,"abolobur"):
    print("Matched")
'''



import re

pattern = r"a$"
if re.match(pattern,"a"):
    print("Matched")






