# Python Bangla Tutorials 54 | Inheritance

class Phone:
    def call(self):
        print("You Can Call")

    def messege(self):
        print("You Can Message")


class samsung(Phone):

    def photo(self):
        print("You Can Take Photo")

s = samsung()
s.call()
s.messege()
s.photo()






