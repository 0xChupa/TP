import pygame
from pygame.locals import *

pygame.init()
x = 640
y = 480
#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((x, y))
fenetre = pygame.display.set_mode((x,y), RESIZABLE)
#fenetre = pygame.display.set_mode((640,480), FULLSCREEN)
#Chargement et collage du fond
#fond = pygame.image.load("back.jpg").convert()
#fenetre.blit(fond, (0,0))

bingo = pygame.image.load("bingooo.jpg").convert()
#bingo.set_colorkey((255,255,255))
fenetre.blit(bingo, (15,15))

Roulette = pygame.image.load("Roulette.jpg").convert()
fenetre.blit(Roulette, (441,15))

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN and event.key == K_SPACE:
            continuer = 0

        if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 15 and event.pos[0] < 199 and event.pos[1] > 15 and event.pos[1] < 103:
            print("début du bingo...")

        if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 441 and event.pos[0] < 625 and event.pos[1] > 15 and event.pos[1] < 103:
            print("début de la Roulette...")


