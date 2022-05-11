import array
import random

balance = input("Avec combien commencez-vous à jouer ? ")

choicesP = [i for i in range(1,90)]
choicesB = [i for i in range(1,90)]
randomNumList = [i for i in range(1,90)]

def check(list): 
    return all(i == list[0] for i in list) 

playBoardP = [         #P pour Player
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]

playBoardB = [         # B pour Bot
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]

for i in range(5):
        for j in range(5):
            choiceP = random.choice(choicesP)       #Remplissage du Tableau Player
            playBoardP[i][j] = choiceP
            choicesP.pop(choicesP.index(choiceP))

            choiceB = random.choice(choicesB)       #Remplissage du Tableau Bot
            playBoardB[i][j] = choiceB
            choicesB.pop(choicesB.index(choiceB))


mise = input("Quelle est votre mise ? ")
while int(mise) > int(balance):
    mise = input("Votre mise est supérieure à votre balance. Rentrez une nouvelle mise : ")
balance = int(balance) - int(mise)

for i in range (5):
    print(str(playBoardP[i]) + "             "   + str(playBoardB[i]))

while check(playBoardB) == False and check(playBoardP) == False:
    randomNum = random.choice(randomNumList)
    randomNumList.pop(randomNumList.index(randomNum))
    print(randomNum)

    for i in range(5):
        for j in range(5):
            if playBoardP[i][j] == randomNum:
                playBoardP[i][j] = 'X'
            if playBoardB[i][j] == randomNum:
                playBoardB[i][j] = 'X'
            else:
                continue

    for i in range (5):
        print(str(playBoardP[i]) + "             "   + str(playBoardB[i]))
    if check(playBoardB) == True and check(playBoardP) == True:
        print("Vous avez rempli votre grille en même temps, égalite !")
        balance = int(balance) + int(mise)
        break
    if check(playBoardP) == True:
        print("Vous avez gagné, bien joué !")
        mise = int(mise) * 2
        balance = int(balance) + int(mise)
        break
    if check(playBoardB) == True:
        print("Votre adversaire a gagné, dommage !")