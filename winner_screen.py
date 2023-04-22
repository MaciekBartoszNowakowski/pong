import pygame, sys
from pygame.math import Vector2
from pojedyncze_napisy import tekst
pygame.init()


class winner(object):

    def __init__(self, game, person):
        self.person = person
        self.game = game
        self.screen = game.screen
        self.kto_wygral = tekst(self,640,350,40,' {}'.format(self.person))
        self.co_dalej1 = tekst(self,640,400,30,'ESC - powrot do menu')
        self.co_dalej2 = tekst(self, 640, 440, 30, 'ENTER - Zagraj jeszcze raz')

    def draw(self):
        self.kto_wygral.draw((0, 0, 0), (255, 255, 255))
        self.co_dalej1.draw((0, 0, 0), (255, 255, 255))
        self.co_dalej2.draw((0, 0, 0), (255, 255, 255))

    def tick(self):
        pressed = pygame.key.get_pressed()
        self.game.ball.vel *= 0
        # print(pressed[pygame.K_w])
        if pressed[pygame.K_RETURN]:
            self.game.result = [0, 0]
            self.game.koniec = None
            self.game.ball.vel = Vector2(1, 1)
            return 0
        if pressed[pygame.K_ESCAPE]:
            self.game.result = [-1, -1]
            return 1
