import pygame, sys
from paletka import Paletka
from pilka import Pilka


class Game(object):

    def __init__(self):
        #Config
        self.tps_max=120

        #initialization
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))

        self.box1 = Paletka(self,10,10)
        self.box2 = Paletka(self,1260,10)
        self.ball = Pilka(self,625,355)

        # time
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        while True:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

            # TICKING
            self.tps_delta += self.tps_clock.tick() / 1000.0
            while self.tps_delta > 1 / self.tps_max:
                self.tick()
                self.tps_delta -=1 / self.tps_max

            #drawing
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self):

        self.box1.tick(pygame.K_w,pygame.K_s)
        self.box2.tick(pygame.K_UP,pygame.K_DOWN)
        self.ball.tick()


    def draw(self):
        self.box1.draw(0, 150, 255)
        self.box2.draw(255, 0, 0)
        self.ball.draw()
    #     pygame.draw.rect(self.screen, (15, 255, 15), pygame.Rect(637,357,6,6))





Game()



# ball=pygame.Rect(637,357,6,6)
#
# b_spin=1
# rpion=b_spin
# rpoz=b_spin
# max_tps=120
# odb=0
# dt=0.0
#
#
#
#
#     while delta > 1/max_tps:
#
#     # INPUT
#         if pygame.key.get_pressed() [pygame.K_s]:
#             if box1.y + box1.height < rez[1]:
#                 box1.y += 4
#         if pygame.key.get_pressed() [pygame.K_w]:
#             if box1.y >0:
#                 box1.y -= 4
#
#         if pygame.key.get_pressed() [pygame.K_DOWN]:
#             if box2.y + box2.height < rez[1]:
#                 box2.y += 4
#         if pygame.key.get_pressed() [pygame.K_UP]:
#             if box2.y >0:
#                 box2.y -= 4
#
#
#         # odbicia piłki
#
#         # sufit i podloga
#         if ball.y +ball.height > rez[1]:
#             rpion= -b_spin
#             if rpoz < 0:
#                 rpoz = -b_spin
#             else:
#                 rpoz = b_spin
#         if ball.y < 0:
#             rpion= b_spin
#             if rpoz < 0:
#                 rpoz = -b_spin
#             else:
#                 rpoz = b_spin
#
#         # paletka 2
#         if box2.x <= ball.x + ball.width:
#             if ball.y < box2.y + box2.height and ball.y + ball.height > box2.y:
#                 rpoz= -b_spin
#
#         # paletka 1
#         if box1.x + box1.width >= ball.x:
#             if ball.y < box1.y + box1.height and ball.y + ball.height > box1.y:
#                 rpoz= b_spin
#
#
#         # pilka movement
#         ball.x +=rpoz
#         ball.y +=rpion
#         if b_spin < 10:
#             odb += 1
#             if odb > 600:
#                 b_spin += 1
#                 odb = 0
#         delta = 0
#
#
#
#     if ball.x < 0 or ball.x + ball.width > 1280:
#         break


