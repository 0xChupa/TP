import pygame
from pygame import *
import sys

x = 640
y = 480

fenetre = pygame.display.set_mode((x, y))
class Bouton :
    def __init__(self, window, posX, posY, rect, button_color=(100, 100, 100)):
        self.window = window
        self.posX = posX
        self.posY = posY
        self.rect = rect
        self.button_color = button_color

    def drawButton(self, text, fontsize=15, text_color=(150, 150, 150)):
        """Dessine un bouton"""
        myfont = pygame.font.SysFont('Comic Sans MS', fontsize)  # Initialise la police
        textsurface = myfont.render("try" , 1, text_color)
        return pygame.draw.rect(self.window, self.button_color, self.rect, 0) and self.window.blit(textsurface, (
        self.posX, self.posY))  # Affiche bouton+texte


Bouton(fenetre, 320 , 240 , rect , (100,100,100))


pygame.display.flip()

continuer = 1
while continuer:
    for event in pygame.event.get():   #On parcours la liste de tous les événements
        if event.type == QUIT:
            continuer = 0






