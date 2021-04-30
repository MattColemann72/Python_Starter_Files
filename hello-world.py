#I got carried away..

import random

message = "Hello"
name = "Matt"
i = 0
correctNumber = random.randint(1,10)
playerwins = False
#print(correctNumber)

numberSelected = 0

while i < 5:
    i = i+1
    if i == 5:
        name = "Matthew"
    else:
        name = "Matt"
    
userName = str(input("Hi there! Please enter your name "))

print(f"{message}, {userName}. You have 3 chances to choose the correct number between 1 & 10. You must use the indicators to see whether the number is higher or lower than what you last selected.")

input("")

input("If you don't guess correctly the world will end.")

while  numberSelected < 3 and playerwins != True:
    chooseNumber = int(input("Please enter your number now: "))
    if chooseNumber >= 1 and chooseNumber <= 10:
        numberSelected = numberSelected + 1
        if chooseNumber == correctNumber:
            print("Congratulations. You saved the world.")
            playerwins = True
        elif chooseNumber < correctNumber:
            print(">")
        else:
            print("<")
    else:
        print("Your number must be between 1 & 5! Hurry!")

if playerwins == False:
    print("The world has ended. Unlucky chucky.")