import pygame, sys
from paletka import Paletka
from pilka import Pilka
from winner_screen import winner
from tablica_wynikowa import score_table


class Game(object):

    def __init__(self):
        # Config
        self.tps_max = 180

        # initialization
        self.screen = pygame.display.set_mode((1280, 720))

        self.box1 = Paletka(self, 10, 10)
        self.box2 = Paletka(self, 1260, 10)
        self.ball = Pilka(self, 625, 355)
        self.result = [0, 0]
        self.koniec = None
        self.score = score_table(self)

        # time
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            if self.result == [-1, -1]:
                break

            # TICKING
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -= 1 / self.tps_max

            # drawing
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

            # RESET
            if self.ball.poz.x < 0:
                self.ball = Pilka(self, 625, 355)
                self.result[0] += 1
                if self.result[0] == 3:
                    self.koniec = winner(self, 2)

            if self.ball.poz.x > 1280:
                self.ball = Pilka(self, 625, 355)
                self.result[1] += 1
                if self.result[1] == 3:
                    self.koniec = winner(self, 1)

    def tick(self):
        self.box1.tick(pygame.K_w, pygame.K_s)
        self.box2.tick(pygame.K_UP, pygame.K_DOWN)
        self.ball.tick()
        if self.koniec != None:
            self.koniec.tick()

    def draw(self):
        if self.koniec == None:
            self.box1.draw(0, 150, 255)
            self.box2.draw(255, 0, 0)
            self.ball.draw()
            self.score.draw(self.result)
        else:
            self.koniec.draw()


pygame.init()
