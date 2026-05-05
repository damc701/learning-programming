#import library 
from random import randint
import os
#fuctions
def rolldices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2 

#declare and intialize  variables and/or constants
player_lives = 3
dice1 = 0
dice2 = 0
lives = 3 
roll_count = 0
equal_count = 0
status = True
dices_add = 0

# main 
while status:
    os.system('cls')
    dices = rolldices()
    roll_count+=1
    print("#" * 20)
    print(f"roll dices N° .: {roll_count}")
    print("#" *20)
    print(f"player lives: {player_lives}")
    print(f"dice 1: {dices[0]}")
    print(f"dice 2: {dices[1]}")
    dices_add = dices[0] + dices[1]
    print(f"dice add: {dices_add}")

    if dices_add % 2 != 0:
        lives-=1
        print(f"you've lost a live ::: now you have {player_lives} lives")
        if player_lives == 0:
            print(":::GAME OVER:::")
            break

    if roll_count ==5 :
        break
    else :
        press_key = input ("\npress any key to roll dice again")