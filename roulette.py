import random
import pygame
from pygame.locals import *

numbers = [i for i in range(1,36)]  # on crée une liste de nombres
colors = ['rouge', 'noir']

def playRoulette(balance):
    pygame.init()
    x = 640  # Definition de la taille de la fenêtre
    y = 480

    fond_mach = pygame.display.set_mode((x, y))

    fond = pygame.image.load("roulette_neon_finit.jpg").convert()  # Chargement du fond
    fond_mach.blit(fond, (0, 0))  # Position du fond sur la fenêtre

    pygame.display.flip()

    continuer = 1
    while continuer == 1:
        for event in pygame.event.get():  # On parcours la liste de tous les événements

            if event.type == QUIT:
                continuer = 0
                pygame.quit()


            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 12 < event.pos[0] < 179 and 389 < event.pos[
                1] < 470:  # Définition de la zone de clic pour mettre la balance à 100.
                mise = 100
                print("Votre mise est de :", mise)
                continuer = 0

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 231 < event.pos[0] < 401 and 391 < event.pos[
                1] < 473:
                mise = 500
                print("Votre mise est de :", mise)
                continuer = 0

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 455 < event.pos[0] < 617 and 391 < event.pos[
                1] < 467:
                mise = 1000
                print("Votre mise est de :", mise)
                continuer = 0


    while int(mise) > int(balance):     # puis on vérifie qu'elle est cohérente avec la balance
        mise = input("Votre mise est supérieure à votre balance. Rentrez une nouvelle mise. ")
    while int(mise) > 1000 or int(mise) < 1:
        mise = input("Votre mise ne respecte pas les conditions. Rentrez une nouvelle mise. ")
    choice = input("Misez vous sur un numéro (press N) ou une couleur (press C) ? ")    # on demande au joueur ce sur quoi il veut miser (couleur ou nombre)
    if choice.lower() == 'n':   # si il choisi 'nombre'
        numberChoose = input("Entrez votre numéro (entre 1 et 36) ")    # alors on lui demande lequel entre 1 et 36
        while int(numberChoose) not in numbers:
            numberChoose = input("Votre numéro doit être compris entre 1 et 36 ! ")     # avant de vérifier si le numéro respecte le critère
        balance = int(balance) - int(mise)
        winningNumber = random.choice(numbers)  # on tire un nombre aléatoire entre 1 et 36
        if numberChoose == winningNumber:   # si les 2 nombres correspondent
            gain = int(mise) * 34
            mise = int(mise) * 35       # le joueur repart avec un multiplicateur *35
            balance = int(balance) + int(mise)
            print("Félicitations, vous repartez avec un gain de " + str(gain) + " !")
            return balance
        else:
            print("Dommage, c'est perdu ! Le numéro gagnant était : " + str(winningNumber))
            return balance
    if choice.lower() == 'c':       # même principe pour les couleurs
        balance = int(balance) - int(mise)
        colorChoose = input("Entrez votre couleur (rouge ou noir) : ")
        winningColor = random.choice(colors)
        if colorChoose == winningColor:
            gain = int(mise)
            mise = int(mise) * 2    # la multiplicateur sera jsute moins élevé, mais le principe précédent est similaire à celui pour les nombres
            balance = int(balance) + int(mise)
            print("C'est gagné, vous repartez avec un gain de : " + str(gain) + " !")
            return balance
        else:
            print("Dommage, c'est perdu !")
            return balance

            # la fonction renvoie la balance actualisée.