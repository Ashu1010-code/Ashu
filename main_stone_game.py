'''

Stone 0 
paper 1
scijar -1

'''

import random


computer = random.choice([1,0,-1])

youstr = input("Enter your choices : ")
youDict =  {'s' : 0 , 'p' : 1 , 'sc' : -1}
reverseDict = {0 : "Stone" ,1 : "Paper"  , -1 : "Scijar"}
you = youDict[youstr]

print(f"Your choice {reverseDict[you]}\nComputer choice {reverseDict[computer]}😔")  #computer - you



if (computer == you):
    print("Draw the game.\nPlay the game again" )

elif(computer == 1 and you == 0 ): # 1 
    print("You lose👍😔")

elif(computer == 1 and you == -1 ): # 2
    print("You win👍")

elif(computer == -1 and you == 0 ): # -1
    print("You win👍")

elif(computer == -1 and you == 1): # -2
    print("You lose👍😔")

elif(computer == 0 and you == 1 ): # -1
    print("You win👍")

elif(computer == 0 and you == -1 ): # 1
    print("You lose👍😔")

else:
    print("something is worrg.\nTry again!")