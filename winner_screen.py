import pygame, sys
from pygame.math import Vector2

pygame.init()


class winner(object):

    def __init__(self, game, person):
        self.person = person
        self.game = game

    def draw(self):
        black = (0, 0, 0)
        white = (255, 255, 255)
        self.game.screen.fill((0, 0, 0))
        x = 1280
        y = 720
        font = pygame.font.Font('freesansbold.ttf', 32)
        tresc = 'Wygrał gracz numer {}'.format(self.person)
        text = font.render(tresc, True, white, black)
        textRect = text.get_rect()
        textRect.center = (x // 2, y // 2)
        self.game.screen.blit(text, textRect)

    def tick(self):
        pressed = pygame.key.get_pressed()
        self.game.ball.vel *= 0
        # print(pressed[pygame.K_w])
        if pressed[pygame.K_w]:
            self.game.result = [0, 0]
            print("BAJO")
            self.game.koniec = None
            print("BAJO JAJO", self.game.koniec)
            self.game.ball.vel = Vector2(1, 1)
            return 0
        if pressed[pygame.K_ESCAPE]:
            self.game.result = [-1, -1]
            return 1
