# Python Bangla Tutorials 29 : Guessing Game
from random import randint

for x in range(1,200):
    guessNumber = int(input("Enter You Gase Between 1 to 20 : "))
    randomNumber = randint(1,20)

    if guessNumber == randomNumber:
       print("You Have Won")
       print("Congratulations !!!")

    else:
       print("You Have Lost")
       print("Try Again")
       print("Correct Random Number : ",randomNumber)


