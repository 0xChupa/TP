import pygame
from pygame.locals import *
from bingo import playBingo
from blackjack import playBlackjack
from machineSous import playMachineSous
from roulette import playRoulette
import sys
import time

balance = input("Quelle est votre balance ? ")

pygame.init()
x = 640  # Definition de la taille de la fenêtre
y = 480

fenetre2 = pygame.display.set_mode((x, y))

fond = pygame.image.load("fond.jpg").convert()  # Chargement du fond
fenetre2.blit(fond, (0, 0))  # Position du fond sur la fenêtre

bingo = pygame.image.load("petitfinn.png").convert()  # Chargement du logo "petitfinn.png"
fenetre2.blit(bingo, (0, 0))

Roulette = pygame.image.load("Roulette.jpg.jpg").convert()
fenetre2.blit(Roulette, (441, 15))

Blackjack = pygame.image.load("BJ.jpg").convert()
fenetre2.blit(Blackjack, (15, 330))

Machine = pygame.image.load("Rr.jpg").convert()
fenetre2.blit(Machine, (500, 280))

file = 'musique.mp3'
pygame.mixer.init()
musique = pygame.mixer.music.load("musique.mp3")
pygame.mixer.music.play()

# Rafraîchissement de l'écran
pygame.display.flip()

# BOUCLE INFINIE
continuer = 1
while continuer == 1:
    #balance = input("Quelle est votre balance ? ")
    pygame.init()
    changeGame = 'P'
    while changeGame.lower() != 's':  # Tant que le joueur souhaite continuer à jouer
        for event in pygame.event.get():  # On parcours la liste de tous les événements
            if event.type == QUIT:
                continuer1 = 0
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer1 = 0

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 15 and event.pos[0] < 180 and \
                    event.pos[1] > 15 and event.pos[1] < 120:  # définition de la zone de clic pour accéder au bingo.
                pygame.mixer.music.stop()
                changeGame = 'P'
                continuer = 0
                while changeGame.lower() == 'p':
                    balance = playBingo(balance)  # Execution du jeu du Bingo.
                    print("Votre balance est : " + str(balance) + "\n")
                    changeGame = input("Voulez-vous continuer (press P), changer de jeu (press C) ou arrêter (press S).")

                if changeGame.lower() == 'c':
                    game = input("A quel jeu veux-tu jouer ? ")

                if changeGame.lower() == 's':
                    print("Merci d'avoir joué, à bientôt !")
                    pygame.quit()
                    exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 441 and event.pos[0] < 625 and \
                    event.pos[1] > 15 and event.pos[1] < 103:
                pygame.mixer.music.stop()
                changeGame = 'P'
                continuer = 0
                while changeGame.lower() == 'p':
                    balance = playRoulette(balance)
                    print("Votre balance est : " + str(balance) + "\n")
                    changeGame = input("Voulez-vous continuer (press P), changer de jeu (press C) ou arrêter (press S).")

                if changeGame.lower() == 'c':
                    game = input("A quel jeu veux-tu jouer ? ")

                if changeGame.lower() == 's':
                    print("Merci d'avoir joué, à bientôt !")
                    pygame.quit()
                    exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 0 and event.pos[0] < 199 and \
                    event.pos[1] > 250 and event.pos[1] < 450:
                pygame.mixer.music.stop()
                changeGame = 'P'
                continuer = 0
                while changeGame.lower() == 'p' :
                    balance = playBlackjack(balance)
                    print("Votre balance est : " + str(balance) + "\n")
                    changeGame = input("Voulez-vous continuer (press P), changer de jeu (press C) ou arrêter (press S).")

                if changeGame.lower() == 'c':
                    game = input("A quel jeu veux-tu jouer ? ")

                if changeGame.lower() == 's':
                    print("Merci d'avoir joué, à bientôt !")
                    pygame.quit()
                    exit()

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 500 and event.pos[0] < 630 and \
                    event.pos[1] > 250 and event.pos[1] < 450:
                pygame.mixer.music.stop()
                changeGame = 'P'
                continuer = 0
                while changeGame.lower() == 'p':
                    balance = playMachineSous(balance)
                    print("Votre balance est : " + str(balance) + "\n")

                    changeGame = input("Voulez-vous continuer (press P), changer de jeu (press C) ou arrêter (press S).")

                if changeGame.lower() == 'c':
                    game = input("A quel jeu veux-tu jouer ? ")

                if changeGame.lower() == 's':
                    print("Merci d'avoir joué, à bientôt !")
                    pygame.quit()
                    exit()

    if balance <= 0:
        print("\nVotre balance est nulle. Vous ne pouvez plus jouer.")
        print("A bientôt.")
