import pygame
from pygame.locals import *
from bingo import playBingo
from blackjack import playBlackjack
from machineSous import playMachineSous
from roulette import playRoulette
import sys
import time



pygame.init()
x = 640  # Definition de la taille de la fenêtre
y = 480

fenetre2 = pygame.display.set_mode((x, y))

fond = pygame.image.load("fond.jpg").convert()  # Chargement du fond
fenetre2.blit(fond, (0, 0))  # Position du fond sur la fenêtre

bingo = pygame.image.load("image_bingo.jpg").convert()  # Chargement du logo "petitfinn.png"
fenetre2.blit(bingo, (15, 15))

Roulette = pygame.image.load("image_roulette.jpg").convert()
fenetre2.blit(Roulette, (475, 15))

Blackjack = pygame.image.load("image_blackjack.jpg").convert()
fenetre2.blit(Blackjack, (15, 340))

Machine = pygame.image.load("image_MachineSous.jpg").convert()
fenetre2.blit(Machine, (451, 329))

Bouton_100 = pygame.image.load("Bouton_100.jpg")
fenetre2.blit(Bouton_100, (207,y-149))
rect100 = Bouton_100.get_rect()

Bouton_500 = pygame.image.load("Bouton_500.jpg")
fenetre2.blit(Bouton_500, (333,y-149))
rect500 = Bouton_500.get_rect()

Bouton_1000 = pygame.image.load("Bouton_1000.jpg")
fenetre2.blit(Bouton_1000, (270,y-88))
rect1000 = Bouton_1000.get_rect()

file = 'musique.mp3'
pygame.mixer.init()
musique = pygame.mixer.music.load("musique.mp3")                # Lancement de la musique lors de l'ouverture de la fenêtre Pygame
pygame.mixer.music.play()

# Rafraîchissement de l'écran
pygame.display.flip()



# BOUCLE INFINIE
continuer = 1
while continuer == 1:
    pygame.init()
    changeGame = 'P'
    while changeGame.lower() == 'p' or changeGame.lower() == 'c' : # Tant que le joueur souhaite continuer à jouer au même jeu ou changer de jeu
        for event in pygame.event.get():  # On parcours la liste de tous les événements

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 207 < event.pos[0] < 307 and 331 < event.pos[
                1] < 387:
                balance = 100

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 333 < event.pos[0] < 433 and 331 < event.pos[
                1] < 387:
                balance = 500

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 270 < event.pos[0] < 370 and 392 < event.pos[
                1] < 448:
                balance = 1000

            if event.type == MOUSEBUTTONDOWN and event.button == 3 and 15 < event.pos[0] < 189 and 15 < event.pos[1] < 149 : # définition de la zone de clic pour accéder au bingo.
                pygame.mixer.music.stop()
                changeGame = 'P'
                continuer = 0
                while changeGame.lower() == 'p':
                    balance = playBingo(balance)  # Execution du jeu du Bingo.
                    print("Votre balance est : " + str(balance) + "\n")
                    changeGame = input("Voulez-vous continuer (press P), changer de jeu (press C) ou arrêter (press S).")

                if changeGame.lower() == 's':                   # Arrêt du jeu sur demande
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

                if changeGame.lower() == 's':
                    print("Merci d'avoir joué, à bientôt !")
                    pygame.quit()
                    exit()

            if changeGame.lower() == 'c':
                game = input("A quel jeu veux-tu jouer ? ")
                if game.lower() == 'roulette':
                    balance = playRoulette(balance)

                elif game.lower() == 'blackjack':
                    balance = playBlackjack(balance)

                elif game.lower() == 'machine a sous' or game.lower() == 'machine à sous':
                    balance = playMachineSous(balance)

                elif game.lower() == 'bingo':
                    balance = playBingo(balance)

                else:
                    print("Ce jeu n'existe pas, veuillez réessayer")

                changeGame = input("Voulez-vous continuer (press P), changer de jeu (press C) ou arrêter (press S).")

                if balance <= 0:
                    print("\nVotre balance est nulle. Vous ne pouvez plus jouer.")
                    print("A bientôt.")
