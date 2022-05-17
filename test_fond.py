import pygame
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("back.jpg").convert()
fenetre.blit(fond, (0,0))

perso = pygame.image.load("bingo.jpg").convert()
fenetre.blit(perso, (20,30))

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

        if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[1] < 100:
            print("Zone dangereuse")


