import random
import pygame
from pygame.locals import *
symbol = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6]

def test():
    test =  random.choice(symbol)
    return test


def playMachineSous(balance):
    symb1 = test()
    symb2 = test()
    symb3 =  test()

    pygame.init()
    x = 640  # Definition de la taille de la fenêtre
    y = 480

    fond_mach = pygame.display.set_mode((x, y))

    fond = pygame.image.load("Machine_neon_finit.jpg").convert()  # Chargement du fond
    fond_mach.blit(fond, (0, 0))  # Position du fond sur la fenêtre.

    pygame.display.flip()

    continuer = 1
    while continuer == 1:
        for event in pygame.event.get():  # On parcours la liste de tous les événements

            if event.type == QUIT:
                continuer = 0
                pygame.quit()

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 150 < event.pos[0] < 227 and 228 < event.pos[
                1] < 293:   # Définition de la zone de clic pour mettre la balance à 100.
                mise = 100
                print("Votre mise est de :" , mise)
                continuer = 0

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 251 < event.pos[0] < 324 and 228 < event.pos[
                1] < 293:
                mise = 500
                print("Votre mise est de :" , mise)
                continuer = 0

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 341 < event.pos[0] < 416 and 228 < event.pos[
                1] < 293:
                mise = 1000
                print ("Votre mise est de :" , mise)
                continuer = 0



    while int(mise) > int(balance):
        mise = input("Votre mise est supérieure à votre balance. Rentrez une nouvelle mise : ") 

    balance = int(balance) - int(mise)  # on actualise la balance

    print("Les symboles sont : " + str(symb1) + " / " + str(symb2) + " / " + str(symb3) )

    if symb1 == symb2 == symb3:     # on vérifie si les 3 symboles sont similaires
        print("Bien joué, vous avez gagné !")
        if symb1 == 1:  
            mise = int(mise) * 2    # on adapte les multiplicateurs en fonction du symbole.
            balance = int(balance) + int(mise)
            return balance
        if symb1 == 2:
            mise = int(mise) * 3
            balance = int(balance) + int(mise)
            return balance
        if symb1 == 3:
            mise = int(mise) * 5
            balance = int(balance) + int(mise)
            return balance
        if symb2 == 4:
            mise = int(mise) * 10
            balance = int(balance) + int(mise)
            return balance
        if symb2 == 5:
            mise = int(mise) * 20
            balance = int(balance) + int(mise)
            return balance
        if symb2 == 6:
            mise = int(mise) * 50
            balance = int(balance) + int(mise)
            return balance
    else:
        print("Vous avez perdu, dommage !")
        return balance