import pygame, sys


class tekst(object):

    def __init__(self, menu,x,y,size,words):
        self.menu=menu
        self.x=x
        self.y=y
        self.size=size
        self.words=words



    def draw(self,background,color):
        font = pygame.font.Font('freesansbold.ttf', self.size)
        text = font.render(self.words, True, color, background)
        multiRect = text.get_rect()
        multiRect.center = (self.x, self.y)
        self.menu.screen.blit(text, multiRect)