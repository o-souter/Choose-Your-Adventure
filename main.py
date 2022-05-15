import os
import time
from turtle import clear
def clearScreen():
    os.system('cls||clear')

def wip():
    print("Pathway Unfinished: Work still in progress! Thank you for getting this far!")

answer = input("Would you like to enter? (y/n)")

if answer.lower().strip() == "y":
    clearScreen()
    print("It is the year 2063. You are Jodin the Traveller and are stuck in a Zombie infested world. After losing your last hideout you are on the search for somewhere safe, maybe even the lands that lie behind the great walls.")
    time.sleep(3)
    answer = input("You reach a crossroads, a river flows in front of you. \nWill you go left or right? ").lower().strip()
    #print(answer)
    
    if answer == "left":
        #YOU GO LEFT
        clearScreen()
        answer = input("A man approaches you. He is holding a gun. \nWill you attack or run? ").lower().strip()
        if answer == "attack":
            #YOU ATTACK
            clearScreen()
            print("The man fires two shots into your chest. You fall to the ground.\nYou Died.")
        elif answer =="run":
            #YOU RUN
            clearScreen()
            print("You start running from the man. He shouts after you and you hear bullets whizz over your head. After a while you slow your pace, making sure the man no longer is following.")
            time.sleep(2)
            answer = input("You come across a convenience store on the side of the road. Will you risk entering to forage for supplies? (y/n) ").lower().strip()
            if answer == "y" :
                #YOU ENTER THE STORE
                print("You approach the store quietly. Looking through the door you spot two zombies. One is missing an arm and the other is wearing a bulletproof vest and riot visor. Outside the store there are some rocks.")
                time.sleep(3)
                answer = input("Will you attack or distract the zombies? ").lower().strip()
                if answer == "attack":
                    #YOU ATTACK THE ZOMBIES
                    print("You push the door open and begin tossing rocks at the two zombies. To your surprise they begin running at you.")
                    time.sleep(1)
                    print("Between two rocks you manage to crush the skull of the first zombie. In these few seconds, the second zombie bites your arm. You manage to hit it hard enough in the head to kill it. It falls to the ground.")
                    time.sleep(10)
                    
                    print("You decide to search the store for supplies")
                    answer = input("The store contains a food aisle, toilets and cashiers. Where do you search first? ").lower().strip()
                    if answer == "food aisle":
                        #YOU CHECK THE FOOD AISLE
                        clearScreen()
                        print("You run to the food aisle. The stench of rotting food immediately hits you in the face. There are bags of crisps, sweets and bottles of water. You load all of these into your backpack hastily.")
                        time.sleep(3)
                        print("Exhausted, your vision begins to blur and you collapse to the floor.")
                        time.sleep(1)
                        print("Hours later, you crookidly reanimate. You have become a Zombie!")
                        time.sleep(3)
                        print("You Died")
                    elif answer == "toilets":
                        #YOU CHECK THE TOILETS
                        clearScreen()
                        print("You walk over to the toilets. The smell is vile. A medical station is attached to the wall on your left. You open it, hoping to find something for the Zombie bite.")
                        time.sleep(1)
                        answer = input("In the medical station you see 3 items: Bandages, Antibiotics and Painkillers. Which one will you take first? ").lower().strip()
                        if answer == "bandages":
                            #YOU TAKE THE BANDAGES
                            print("You wrap bandages lazily around your hand. This does very little as the bite didn't draw much blood.")
                            time.sleep(3)
                            print("You begin to feel dizzy and collapse to the floor of the store.")
                            time.sleep(1)
                            print("Hours later, you crookidly reanimate. You have become a Zombie!")
                            time.sleep(3)
                            print("You Died")

                        elif answer == "painkillers":
                            #YOU TAKE THE PAINKILLERS
                            print("You take the painkillers.")
                            time.sleep(3)
                            print("You begin to feel dizzy and collapse to the floor of the store.")
                            time.sleep(1)
                            print("Hours later, you crookidly reanimate. You have become a Zombie! at least you aren't sore though.")
                            time.sleep(3)
                            print("You Died a not very painful death")
                        
                        elif answer == "antibiotics":
                            #YOU TAKE THE ANITBIOTICS
                            print("You take the antibiotics")
                            time.sleep(5)
                            print("After a few minutes you start to feel better. You pocket the rest of the supplies, saving them for later")
                            time.sleep(3)
                            print("You exit the store")
                            wip()
                elif answer == "distract":
                    wip()    
            else:
                print("You keep walking down the path. You look behind you and notice a zombie in pursuit")
                answer = input("What do you do? Attack or run? ").lower().strip()
                if answer == "attack":
                    wip()
                elif answer == "run":
                    wip()
    elif answer == "right":
        #YOU GO RIGHT
        clearScreen()
        print("You turn right")
        wip()
    else:
        clearScreen()
        print("You stride confidently into the flowing river and drown. Not sure what you expected to happen.\nYou Died.")


else:
    print("...")