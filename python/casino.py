#import library 
from random import randint
import os
#fuctions
def rolldices():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return dice1, dice2 

#declare and intialize  variables and/or constants
dice1 = 0
dice2 = 0
lives = 3 
roll_count = 0
equal_count = 0
status = True

# main 
while status:
    os.system('cls')
    dices = rolldices()
    roll_count+=1
    print(f"dice 1: {dices[0]}")
    print(f"dice 2: {dices[1]}")
    if roll_count ==5 :
        break
    else :
        press_key = input ("\npress any key to roll dice again")