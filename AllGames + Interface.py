from bingo import playBingo
from blackjack import playBlackjack
from machineSous import playMachineSous
from roulette import playRoulette
import pygame
from pygame.locals import *

pygame.init()
x = 640
y = 480

fenetre = pygame.display.set_mode((x, y))
fenetre = pygame.display.set_mode((x,y), FULLSCREEN)

fond = pygame.image.load("fond.jpg").convert()
fenetre.blit(fond, (0,0))

bingo = pygame.image.load("petitfinn.png").convert()
bingo.set_colorkey((0,0,0))
fenetre.blit(bingo, (0,0))

Roulette = pygame.image.load("Roulette.jpg.jpg").convert()
fenetre.blit(Roulette, (441,15))

Blackjack = pygame.image.load("BJ.jpg").convert()
fenetre.blit(Blackjack, (15,330))

Machine = pygame.image.load("Rr.jpg").convert()
fenetre.blit(Machine, (441,280))

file = 'musique.mp3'
musique = pygame.mixer.music.load("musique.mp3")
pygame.mixer.music.play()

#Rafraîchissement de l'écran
pygame.display.flip()

#game = input("A quel jeu veux-tu jouer ? ")
balance = input("Quelle est votre balance ? ")
changeGame = 'P'

while changeGame.lower() != 's':
    if game.lower() == 'bingo':
        balance = playBingo(balance)
        if balance <= 0:
            break
        print("Votre balance est : " + str(balance) + "\n")
    if game.lower() == 'blackjack':
        balance = playBlackjack(balance)
        if balance <= 0:
            break
        print("Votre balance est : " + str(balance) + "\n")
    if game.lower() == 'machinesous':
        balance = playMachineSous(balance)
        if balance <= 0:
            break
        print("Votre balance est : " + str(balance) + "\n")
    if game.lower() == 'roulette':
        balance = playRoulette(balance)
        if balance <= 0:
            break
        print("Votre balance est : " + str(balance) + "\n")
    changeGame = input("Voulez-vous continuer (press P), changer de jeu (press C) ou arrêter (press S).")
    print("\n")
    if changeGame.lower() == 'p':
        continue
    if changeGame.lower() == 'c':
        game = input("A quel jeu veux-tu jouer ? ")

if balance <= 0:
    print("\nVotre balance est nulle. Vous ne pouvez plus jouer.")
print("A bientôt.")