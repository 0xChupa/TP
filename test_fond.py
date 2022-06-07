import pygame
from pygame.locals import *

pygame.init()
x = 640
y = 480



fenetre = pygame.display.set_mode((x, y))
#fenetre = pygame.display.set_mode((x,y), FULLSCREEN)

#Chargement et collage du fond
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

input_rect = pygame.Rect(200, 200, 140, 32)

#Rafraîchissement de l'écran
pygame.display.flip()

#BOUCLE INFINIE
continuer = 1
while continuer:
    for event in pygame.event.get():   #On parcours la liste de tous les événements
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            continuer = 0

        if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 15 and event.pos[0] < 180 and event.pos[1] > 15 and event.pos[1] < 120:
            pygame.mixer.music.stop()
            print("début du bingo...")

        if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 441 and event.pos[0] < 625 and event.pos[1] > 15 and event.pos[1] < 103:
            print("début de la Roulette...")
            pygame.mixer.music.stop()

        if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 0 and event.pos[0] < 199 and event.pos[1] > 250 and event.pos[1] < 450:
            print("début du blackjack...")
            pygame.mixer.music.stop()

        if event.type == MOUSEBUTTONDOWN and event.button == 3 and event.pos[0] > 441 and event.pos[0] < 625 and event.pos[1] > 250 and event.pos[1] < 450:
            print("début de la machine à sous...")
            pygame.mixer.music.stop()

