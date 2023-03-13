import pygame
from pygame.math import Vector2

class Pilka(object):

    def __init__(self, game, x, y):
        self.game = game
        self.poz = Vector2(x, y)
        self.vel = Vector2(1, 1)

    def tick(self):
        #physic
        #speed
        self.poz += self.vel
        # deflection and acceleration
        if self.poz.y > 720:
            self.vel.y *= -1
            if self.poz.y > -10:
                self.vel *= 1.2
        if self.poz.y < 0:
            self.vel.y *= -1
            if self.poz.y > -10:
                self.vel *= 1.2

    def draw(self):
        r, g, b = 20, 255, 20
        rect = pygame.Rect(self.poz.x, self.poz.y, 10, 10)
        pygame.draw.rect(self.game.screen, (r, g, b), rect)
