import pygame
from pygame.locals import *

from bingo import playBingo
from blackjack import playBlackjack
from machineSous import playMachineSous
from roulette import playRoulette

pygame.init()
x = 640  # Definition de la taille de la fenêtre
y = 480

fenetre = pygame.display.set_mode((x, y))
# fenetre = pygame.display.set_mode((x,y), FULLSCREEN)


fond = pygame.image.load("fond.jpg").convert()  # Chargement du fond
fenetre.blit(fond, (0, 0))  # Position du fond sur la fenêtre

bingo = pygame.image.load("petitfinn.png").convert()  # Chargement du logo "petitfinn.png"
fenetre.blit(bingo, (0, 0))

Roulette = pygame.image.load("Roulette.jpg.jpg").convert()
fenetre.blit(Roulette, (441, 15))

Blackjack = pygame.image.load("BJ.jpg").convert()
fenetre.blit(Blackjack, (15, 330))

Machine = pygame.image.load("Rr.jpg").convert()
fenetre.blit(Machine, (441, 280))

file = 'musique.mp3'
pygame.mixer.init()
musique = pygame.mixer.music.load("musique.mp3")
pygame.mixer.music.play()

# Rafraîchissement de l'écran
pygame.display.flip()

# BOUCLE INFINIE
continuer = 1
while continuer == 1:
    balance = input("Quelle est votre balance ? ")
    changeGame = 'P'
    while changeGame.lower() != 's':  # Tant que le joueur souhaite continuer à jouer
        for event in pygame.event.get():  # On parcours la liste de tous les événements
            if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 15 and event.pos[0] < 180 and \
                    event.pos[1] > 15 and event.pos[1] < 120:  # définition de la zone de clic pour accéder au bingo.
                # pygame.mixer.music.stop()
                # pygame.quit()
                changeGame = 'P'
                continuer = 0
                balance = playBingo(balance)  # Execution du jeu du Bingo.
                print("Votre balance est : " + str(balance) + "\n")

                changeGame = input("Voulez-vous continuer (press P), changer de jeu (press C) ou arrêter (press S).")

                if changeGame.lower() == 'c':
                    game = input("A quel jeu veux-tu jouer ? ")

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 441 and event.pos[0] < 625 and \
                    event.pos[1] > 15 and event.pos[1] < 103:
                # pygame.mixer.music.stop()
                # pygame.quit()
                changeGame = 'P'
                continuer = 0
                balance = playRoulette(balance)
                print("Votre balance est : " + str(balance) + "\n")

                changeGame = input("Voulez-vous continuer (press P), changer de jeu (press C) ou arrêter (press S).")

                if changeGame.lower() == 'c':
                    game = input("A quel jeu veux-tu jouer ? ")

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 0 and event.pos[0] < 199 and \
                    event.pos[1] > 250 and event.pos[1] < 450:
                # pygame.mixer.music.stop()
                # pygame.quit()
                changeGame = 'P'
                continuer = 0
                balance = playBlackjack(balance)
                print("Votre balance est : " + str(balance) + "\n")

                changeGame = input("Voulez-vous continuer (press P), changer de jeu (press C) ou arrêter (press S).")

                if changeGame.lower() == 'c':
                    game = input("A quel jeu veux-tu jouer ? ")

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 441 and event.pos[0] < 625 and \
                    event.pos[1] > 250 and event.pos[1] < 450:
                # pygame.mixer.music.stop()
                # pygame.quit()
                changeGame = 'P'
                continuer = 0
                balance = playMachineSous(balance)
                print("Votre balance est : " + str(balance) + "\n")

                changeGame = input("Voulez-vous continuer (press P), changer de jeu (press C) ou arrêter (press S).")

                if changeGame.lower() == 'c':
                    game = input("A quel jeu veux-tu jouer ? ")

    if balance <= 0:
        print("\nVotre balance est nulle. Vous ne pouvez plus jouer.")
        print("A bientôt.")
