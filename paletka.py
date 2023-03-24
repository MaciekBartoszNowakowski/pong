import pygame
import random
from pygame.math import Vector2


class Paletka(object):

    def __init__(self, game, x, y):
        self.game = game
        self.poz = Vector2(x, y)
        self.vel = Vector2(0.0)

    def tick(self, gora, dol):
        # input
        pressed = pygame.key.get_pressed()
        if pressed[gora] and self.poz.y > 0:
            self.vel = Vector2(0, -3)
        if pressed[dol] and self.poz.y < 620:
            self.vel = Vector2(0, 3)

        # physic
        self.poz += self.vel
        self.vel *= 0

        # deflection
        if self.game.ball.poz.y > self.poz.y and self.game.ball.poz.y + 10 < 100 + self.poz.y:
            if self.poz.x < self.game.ball.poz.x + 10 and self.poz.x + 11 > self.game.ball.poz.x:
                if self.game.ball.vel.x < 4 and self.game.ball.vel.x > -4:
                    self.game.ball.vel *= 1.1
                    self.game.ball.vel.x *= -1
                    self.game.ball.vel.y += random.randint(-10, 10) / 50
                else:
                    self.game.ball.vel.x *= -1

    def draw(self, r, g, b):
        rect = pygame.Rect(self.poz.x, self.poz.y, 11, 100)
        pygame.draw.rect(self.game.screen, (r, g, b), rect)
