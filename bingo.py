import array
import random
import pygame
from pygame.locals import *

def check(list): #  fonction qui vérifie si tous les éléments sont pareils
    return all(i == list[0] for i in list) 

def playBingo(balance):
    choicesP = [i for i in range(1,90)] # liste de nombres de 1 à 90
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

    pygame.init()
    x = 640  # Definition de la taille de la fenêtre
    y = 480

    fond_mach = pygame.display.set_mode((x, y))

    fond = pygame.image.load("bingo_finit.jpg").convert()  # Chargement du fond
    fond_mach.blit(fond, (0, 0))  # Position du fond sur la fenêtre

    pygame.display.flip()

    continuer = 1
    while continuer == 1:
        for event in pygame.event.get():  # On parcours la liste de tous les événements

            if event.type == QUIT:
                continuer = 0
                pygame.quit()

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 13 < event.pos[0] < 143 and 214 < event.pos[
                1] < 312:
                mise = 50
                print("Votre mise est de :", mise)
                continuer = 0

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 92 < event.pos[0] < 221 and 350 < event.pos[
                1] < 446:  # Définition de la zone de clic pour mettre la balance à 100.
                mise = 100
                print("Votre mise est de :", mise)
                continuer = 0

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 377 < event.pos[0] < 508 and 352 < event.pos[
                1] < 447:
                mise = 500
                print("Votre mise est de :", mise)
                continuer = 0

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 487 < event.pos[0] < 605 and 226 < event.pos[
                1] < 317:
                mise = 1000
                print("Votre mise est de :", mise)
                continuer = 0




    while int(mise) > int(balance):
        mise = input("Votre mise est supérieure à votre balance. Rentrez une nouvelle mise : ")
    balance = int(balance) - int(mise)  #   on actualise la balance

    for i in range (5):
        print(str(playBoardP[i]) + "             "   + str(playBoardB[i]))

    while check(playBoardB) == False and check(playBoardP) == False:
        randomNum = random.choice(randomNumList)    # On sélectionne un nombre aléatoire dans la liste
        randomNumList.pop(randomNumList.index(randomNum))   # Puis on le retire de la liste
        print(randomNum)

        for i in range(5):  # on check chaque élément du tableau
            for j in range(5):
                if playBoardP[i][j] == randomNum:   # Si la case correspond au nombre pioché précédemment
                    playBoardP[i][j] = 'X'      # alors on le remplace par 'X'
                if playBoardB[i][j] == randomNum:
                    playBoardB[i][j] = 'X'
                else:
                    continue

        for i in range (5):
            print(str(playBoardP[i]) + "             "   + str(playBoardB[i]))
        if check(playBoardB) == True and check(playBoardP) == True:     # On vérifie si les 2 joueurs ont fini leur grille
            print("Vous avez rempli votre grille en même temps, égalite !")
            balance = int(balance) + int(mise)
            break
        if check(playBoardP) == True:       # On vérifie si le joueur a gagné
            print("Vous avez gagné, bien joué !")
            mise = int(mise) * 2        # Si c'est le cas, sa mise fait *2
            balance = int(balance) + int(mise)
            break
        if check(playBoardB) == True:   #   Si c'est le bot qui gagne, alors la partie est finie.
            print("Votre adversaire a gagné, dommage !")

    return balance