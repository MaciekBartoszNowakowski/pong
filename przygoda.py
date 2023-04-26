import pygame, sys
from paletka import Paletka
from pilka import Pilka
from winner_screen import winner
from AI import high, easy, mid


class adventure(object):

    def __init__(self, menu):
        # Config
        self.tps_max = 180

        # initialization
        self.screen = pygame.display.set_mode((1280, 720))
        self.result = [0,0]

        self.box2 = Paletka(self, 10, 10)
        self.ball = Pilka(self, 30, 60)
        self.blocks = [[None for i in range(30)] for j in range(7)]
        for i in range(7):
            for j in range(7):
                self.blocks[i][23 + j] = Paletka(self, 1203 + 12 * j, 5 + 101 * i)

        self.remaining = 42
        self.koniec = None
        # time
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0
        self.sterowanie = high(self)

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            if self.result == [-1, -1]:
                break
            if self.result == [-2,-2]:
                menu.repeat=True
                break

            # drawing
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

            # TICKING

            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # RESET

            if self.ball.poz.x < 0:
                end = self.koniec = winner(self, "No niestety nie wyszlo")
            # if self.rezult == [-1, -1]:
            #     break

    def tick(self):
        self.box2.tick(pygame.K_w, pygame.K_s)
        # self.sterowanie.sterowanie()
        self.ball.tick()
        for i in range(7):
            for j in range(30):
                if self.blocks[i][j]:
                    if self.blocks[i][j].tick(0, 0, 2) == 1 and j != 29:
                        self.blocks[i][j] = None
                        self.remaining -= 1

        if self.remaining < 1:
            self.koniec = winner(self, "Gratulacje wygrales")

        if self.koniec:
            self.koniec.tick()

    def draw(self):

        if self.koniec:
            self.koniec.draw()
        else:
            self.box2.draw(255, 0, 255)
            for i in range(7):
                for j in range(29):
                    if self.blocks[i][j]:
                        self.blocks[i][j].draw(255, 255, 255)
                self.blocks[i][29].draw(255, 0, 0)
            self.ball.draw()
