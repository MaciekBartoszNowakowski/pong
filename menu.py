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
        font = pygame.font.Font('freesansbold.ttf', 32)
        tresc = ('Nacisnij jeden dla trybu multiplayer')
        text = font.render(tresc, True, self.white, self.black)
        textRect = text.get_rect()
        textRect.center = (self.x // 2, self.y // 2)
        self.screen.blit(text, textRect)


pygame.init()
Menuski()
