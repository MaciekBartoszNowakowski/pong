import pygame, sys
pygame.init()

class winner(object):

    def __init__(self, game, person):
        self.person=person
        self.game=game


    def draw(self):
        black=(0, 0, 0)
        white=(255, 255, 255)
        self.game.screen.fill((0, 0, 0))
        x=1280
        y = 720
        font = pygame.font.Font('freesansbold.ttf', 32)
        tresc='Wygrał gracz numer {}'.format(self.person)
        text = font.render(tresc, True, white, black)
        textRect = text.get_rect()
        textRect.center = (x // 2, y // 2)
        self.game.screen.blit(text, textRect)

        while True:

            pygame.display.flip()



