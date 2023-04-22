import pygame, sys

from multi import Game
from pojedyncze_napisy import tekst
from przygoda import adventure

from wybor import level

class Menuski(object):

    def __init__(self):
        self.tryb = -1
        self.x = 1280
        self.y = 720
        self.screen = pygame.display.set_mode((self.x, self.y))
        self.menopis = tekst(self, self.x // 2, 25, 40, 'MENU')
        self.multi = tekst(self, self.x // 2, 76, 32, 'Nacisnij 1, aby rozpoczac tryb multiplayer')
        self.single = tekst(self, self.x // 2, 126, 32, 'Nacisnij 2, aby rozpoczac tryb singleplayer')
        self.przygoda = tekst(self, self.x // 2, 176, 32, 'Nacisnij 3 aby rozpoczac tryb przygody :-)')

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            # Drawing
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

            # ticking
            self.tick()

    def tick(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_1]:
            Game()
        if pressed[pygame.K_2]:
            pygame.time.wait(100)
            level()
        if pressed[pygame.K_3]:
            adventure()

    def draw(self):
        self.menopis.draw((0, 0, 0), (255, 255, 255))
        self.multi.draw((0, 0, 0), (255, 255, 255))
        self.single.draw((0, 0, 0), (255, 255, 255))
        self.przygoda.draw((0, 0, 0), (255, 255, 255))


pygame.init()
Menuski()
