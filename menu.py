import pygame, sys

from multi import Game


class Menuski(object):

    def __init__(self):
        self.tryb = -1
        self.x = 1280
        self.y = 720
        self.screen = pygame.display.set_mode((self.x, self.y))
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

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

    def draw(self):
        #Napis dotyczący trybu multiplayer
        font = pygame.font.Font('freesansbold.ttf', 32)
        trybmulti = ('Nacisnij jeden dla trybu multiplayer')
        trybmulti = font.render(trybmulti, True, self.white, self.black)
        multiRect = trybmulti.get_rect()
        multiRect.center = (self.x // 2, self.y // 4)
        self.screen.blit(trybmulti, multiRect)


pygame.init()
Menuski()
