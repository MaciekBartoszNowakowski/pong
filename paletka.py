import pygame
import random
from pygame.math import Vector2


class Paletka(object):

    def __init__(self, game, x, y):
        self.game = game
        self.poz = Vector2(x, y)
        self.vel = Vector2(0.0)

    def tick(self, gora, dol, ruch=0):
        # input
        if ruch!=2:
            pressed = pygame.key.get_pressed()
            if pressed[gora] and self.poz.y > 0:
                self.vel = Vector2(0, -3)
            if pressed[dol] and self.poz.y < 620:
                self.vel = Vector2(0, 3)

            # ai input
            if ruch == 1 and self.poz.y > 0:
                self.vel = Vector2(0, -4)
            if ruch == -1 and self.poz.y < 620:
                self.vel = Vector2(0, 4)

        # physic
        self.poz += self.vel
        self.vel *= 0
        # deflection
        if self.game.ball.poz.y > self.poz.y and self.game.ball.poz.y + 10 < 100 + self.poz.y:
            if self.poz.x < self.game.ball.poz.x + 10 and self.poz.x + 11 > self.game.ball.poz.x:
                if self.game.ball.vel.x < 2.8 and self.game.ball.vel.x > -2.8:
                    self.game.ball.vel *= 1.1
                    self.game.ball.vel.x *= -1
                    self.game.ball.vel.y += random.randint(-10, 10) / 50
                    # Debug powodujący, że kiedy piłka uderz w góre, albo dół paletki, to nie zaczyna sie odbijac
                    # wewnątrz niej
                    if self.game.ball.vel.x < 0:
                        self.game.ball.poz.x = self.poz.x - 10
                    else:
                        self.game.ball.poz.x = self.poz.x + 11
                else:
                    self.game.ball.vel.x *= -1
                    if self.game.ball.vel.x < 0:
                        self.game.ball.poz.x = self.poz.x - 10
                    else:
                        self.game.ball.poz.x = self.poz.x + 11

                return 1

    def draw(self, r, g, b):
        rect = pygame.Rect(self.poz.x, self.poz.y, 11, 100)
        pygame.draw.rect(self.game.screen, (r, g, b), rect)
