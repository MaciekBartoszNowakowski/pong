from single import samotny
import pygame, sys
from pojedyncze_napisy import tekst


# class easy(object):
#
#     def __init__(self,game):
#
# class mid(object):
#
#     def __init__(self,game):

class high(object):

    def __init__(self, game):

        self.game = game

        while True:
            self.sterowanie()

    def sterowanie(self):
        if self.game.ball.poz.y > self.game.box2.poz.y:
            self.game.box2.tick(pygame.K_UP, pygame.K_DOWN, -1)
        if self.game.ball.poz.y < self.game.box2.poz.y:
            self.game.box2.tick(pygame.K_UP, pygame.K_DOWN, 1)
        self.game.ball.tick()


class level(object):

    def __init__(self,menu):
        self.x = 1280
        self.y = 720
        self.screen = pygame.display.set_mode((self.x, self.y))
        self.naglowek = tekst(self, self.x // 2, 25, 40, 'POZIOMY')
        self.es = tekst(self, self.x // 2, 76, 32, 'Glupkowaty -- 1')
        self.hard = tekst(self, self.x // 2, 126, 32, 'Godny -- 2')
        self.imposibru = tekst(self, self.x // 2, 176, 32, 'Niezwycezony -- 3')
        self.go_back=False
        self.menu=menu

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            if self.go_back:
                menu.repeat=self.menu
                break


            # Drawing
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

            # ticking
            self.tick()

    def tick(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_1]:
            samotny(1,self,self.menu)
        if pressed[pygame.K_2]:
            samotny(2,self,self.menu)
        if pressed[pygame.K_3]:
            samotny(3,self,self.menu)




    def draw(self):
        self.naglowek.draw((0, 0, 0), (255, 255, 255))
        self.es.draw((0, 0, 0), (255, 255, 255))
        self.hard.draw((0, 0, 0), (255, 255, 255))
        self.imposibru.draw((0, 0, 0), (255, 255, 255))

