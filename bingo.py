import array
import random

choices = [i for i in range(1,50)]
randomNumList = [i for i in range(1,50)]

plateau = [
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
        ]

for i in range(5):
        for j in range(5):
            choice = random.choice(choices)
            plateau[i][j] = choice
            choices.pop(choices.index(choice))

for i in range (5):
    print(plateau[i])

playAgain = 'y'
while playAgain.lower() == 'y':
    randomNum = random.choice(randomNumList)
    randomNumList.pop(randomNumList.index(randomNum))
    print(randomNum)

    for i in range(5):
        for j in range(5):
            if plateau[i][j] == randomNum:
                plateau[i][j] = 'X'
            else:
                continue

    for i in range (5):
        print(plateau[i])
    playAgain = input("Tour Suivant (y/n) ?")