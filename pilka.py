import pygame
from pygame.math import Vector2


class Pilka(object):

    def __init__(self, game, x, y):
        self.game = game
        self.poz = Vector2(x, y)
        self.vel = Vector2(1, 1)

    def tick(self):
        # physic
        # speed
        self.poz += self.vel
        # deflection and acceleration
        if self.poz.y > 710:
            self.vel.y *= -1
            if self.vel.x > -2.8 and self.vel.x < 2.8:
                self.vel *= 1.1
        if self.poz.y < 0:
            self.vel.y *= -1
            if self.vel.x > -2.8 and self.vel.x < 2.8:
                self.vel *= 1.1

    def draw(self):
        r, g, b = 20, 255, 20
        len = 10
        rect = pygame.Rect(self.poz.x, self.poz.y, len, len)
        pygame.draw.rect(self.game.screen, (r, g, b), rect)
