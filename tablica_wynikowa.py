# zajmuje sie wyświetlaniem punktów
import pygame


class score_table(object):

    def __init__(self, game):
        self.game = game
        self.x = 1280
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

    def draw(self, wynik):
        font = pygame.font.Font('freesansbold.ttf', 20)
        trybmulti = ('{} : {}'.format(wynik[0], wynik[1]))
        trybmulti = font.render(trybmulti, True, self.white, self.black)
        multiRect = trybmulti.get_rect()
        multiRect.center = (self.x // 2, 11)
        self.game.screen.blit(trybmulti, multiRect)
