# import packages 

import random
import os

# Funcións 
def draw_dices():
    dc1 = random.randint(1, 6)
    dc2 = random.randint(1, 6)
    return dc1, dc2, dc1 + dc2

def play():
    print(":::NUMBER RACE:::")
    #inputs
    while True :
        try:

            players = int(input("ENTER PLAYERS (2-4): "))
            option = int(input("\nENTER DIFICULT (1-4):\n1.baby(20)\n2.kid(40)\n3.guy(80)\n4.slayer(160)\n: "))
            print("baby(20)\nkid(40)\nguy(80)\nslayer(160)")
            if 2 <= players <= 4 and 1 <= option <= 4:
                break  
            else:
                print("Error: invalid option")
                
        except ValueError:
            print("enter any option")

 #dificult
    if option == 1: meta = 20
    elif option == 2: meta = 40
    elif option == 3: meta = 80
    else: meta = 160

    # Variables
    places = [0] * players
    consecutive = [0] * players
    winner = False

    # game accions 
    while not winner:
        for p in range(players):
            os.system('cls')
            print("#######################")
            print("##### NUMBER RACE #####")
            print("#######################")
            print(f"\n### PLAYER {p+1} TURN ### ")
            dc1, dc2, addicion = draw_dices()
            print(f"\n      ::::dices:::: \n\n{dc1} and {dc2} (addicion: {addicion})\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            places[p] += addicion
            if 1>p<2:
                print(f"\n   player 1 position is: {places[p]}")
                print(f"\n   player 2 position is: {places[p+1]}")
            else:
                print(f"\n   player 1 position is: {places[p-1]}")
                print(f"\n   player 2 position is: {places[p]}")
            # win by finish the line
            if places[p] >= meta:
                print(f"\n!!!!! PLAYER {p+1} WON BY FINISH THE LINE !!!!!")
                winner = True
                break
            else:
                # win by three pairs 
                if dc1 == dc2:
                    consecutive[p] += 1
                    print(f"\nplayer {p+1} have {consecutive[p]} pairs")
                else:
                    consecutive[p] = 0

                if consecutive[p] == 3:
                    print(f"\n!!!!! PLAYER {p+1} WON BY PAIRS !!!!!")
                    winner = True
                    break
            input("\n::press enter to draw dices::")
                
play() 