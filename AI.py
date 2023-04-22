import pygame, sys
import random


class easy(object):

    def __init__(self, game):
        self.game = game
        self.late = 0
        self.ostatni=0

    def sterowanie(self):

        if self.late==0:
            if self.game.ball.poz.y > self.game.box2.poz.y-10:
                self.game.box2.tick(pygame.K_UP, pygame.K_DOWN, -1)
                self.ostatni=-1
            elif self.game.ball.poz.y < self.game.box2.poz.y+10:
                self.game.box2.tick(pygame.K_UP, pygame.K_DOWN, 1)
                self.ostatni=1
            else:
                self.late+=1
                self.game.box2.tick(pygame.K_UP, pygame.K_DOWN, self.ostatni)
                if self.late>5:
                    self.late=0
        else:
            self.late += 1
            self.game.box2.tick(pygame.K_UP, pygame.K_DOWN, self.ostatni)
            if self.late > 10:
                self.late = 0
        self.game.box2.tick(pygame.K_UP, pygame.K_DOWN, self.ostatni)
        self.game.ball.tick()


class mid(object):

    def __init__(self, game):
        self.game = game
        self.late = 10
        self.ostatni = 0

    def sterowanie(self):

        self.late += 1

        if self.late < 10:
            self.game.box2.tick(pygame.K_UP, pygame.K_DOWN, self.ostatni)
        elif self.late < 13:
            self.game.box2.tick(pygame.K_UP, pygame.K_DOWN, 0)
        else:
            if self.game.ball.poz.y > self.game.box2.poz.y:
                self.game.box2.tick(pygame.K_UP, pygame.K_DOWN, -1)
                self.ostatni = -1
            if self.game.ball.poz.y < self.game.box2.poz.y:
                self.game.box2.tick(pygame.K_UP, pygame.K_DOWN, 1)
                self.ostatni = 1

            self.late = 0

        self.game.ball.tick()


class high(object):

    def __init__(self, game):

        self.game = game

    def sterowanie(self):
        if self.game.ball.poz.y > self.game.box2.poz.y:
            self.game.box2.tick(pygame.K_UP, pygame.K_DOWN, -1)
        if self.game.ball.poz.y < self.game.box2.poz.y:
            self.game.box2.tick(pygame.K_UP, pygame.K_DOWN, 1)
        self.game.ball.tick()
