import random

target = random.randint(1,100)

while True:
    userChoice = input("Guess the target or quit :")
    if(userChoice == "quit"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number was too small. take abigger guess..")
    else:
        print("your number was too big. take a smaller guess..")


print("------GAME OVER------")
