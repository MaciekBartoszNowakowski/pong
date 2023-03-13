import pygame
from pygame.math import Vector2

class Paletka(object):

    def __init__(self, game,x,y):
        self.game=game
        self.poz=Vector2(x,y)
        self.vel=Vector2(0.0)

    def tick(self,gora,dol):
        #input
        pressed = pygame.key.get_pressed()
        if pressed[gora] and self.poz.y>0:
            self.vel=Vector2(0,-4)
        if pressed[dol] and self.poz.y < 630:
            self.vel=Vector2(0,4)

        #physic
        self.poz += self.vel
        self.vel*=0


    def draw(self,r,g,b):
        rect=pygame.Rect(self.poz.x,self.poz.y, 10, 90)
        pygame.draw.rect(self.game.screen, (r, g ,b), rect)