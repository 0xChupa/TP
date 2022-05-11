import array
import random

choicesP = [i for i in range(1,90)]
choicesB = [i for i in range(1,90)]
randomNumList = [i for i in range(1,90)]

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

for i in range (5):
    print(str(playBoardP[i]) + "             "   + str(playBoardB[i]))

tourSuivant = 'y'
while tourSuivant.lower() == 'y':
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
    tourSuivant = input("Tour Suivant (y/n) ?")