import pygame, sys
from paletka import Paletka
from pilka import Pilka
from winner_screen import winner
from tablica_wynikowa import score_table
from AI import  high, easy,mid


class samotny(object):

    def __init__(self, poziom):
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

        if poziom == 1:
            self.poziom=easy(self)
        if poziom == 2:
            self.poziom=mid(self)
        if poziom == 3:
            self.poziom=high(self)

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
                    self.koniec = winner(self, 'Wygrał gracz KOMPUTER')

            if self.ball.poz.x > 1280:
                self.ball = Pilka(self, 625, 355)
                self.result[1] += 1
                if self.result[1] == 3:
                    self.koniec = winner(self, 'Wygrał gracz numer 1')

    def tick(self):
        self.box1.tick(pygame.K_w, pygame.K_s)

        # Sterowanie AI
        self.poziom.sterowanie()


        if self.koniec != None:
            self.koniec.tick()
        print(self.ball.vel)

    def draw(self):
        if self.koniec == None:
            self.box1.draw(0, 150, 255)
            self.box2.draw(255, 0, 0)
            self.ball.draw()
            self.score.draw(self.result)
        else:
            self.koniec.draw()


pygame.init()
