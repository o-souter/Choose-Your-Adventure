import os
def clearScreen():
    os.system('cls||clear')

answer = input("Would you like to enter? (y/n)")

if answer.lower().strip() == "y":
    clearScreen()
    answer = input("You reach a crossroads, a river flows in front of you. \nWill you go left or right?").lower().strip()
    #print(answer)
    if answer == "left":
        clearScreen()
        answer = input("A man approaches you. He is holding a gun. \nWill you attack or run?").lower().strip()
        if answer == "attack":
            clearScreen()
            print("The man fires two shots into your chest. You fall to the ground.\nYou Died.")
        elif answer =="run":
            clearScreen()
            print("You start running from the man. He shouts after you and you hear bullets whizz over your head. After a while you slow your pace, making sure the man no longer is following.")
    elif answer == "right":
        clearScreen()
        print("You turn right")
    else:
        clearScreen()
        print("You stride confidently into the flowing river and drown. Not sure what you expected to happen.\nYou Died.")


else:
    print("...")