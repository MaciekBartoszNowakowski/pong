# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame, sys

pygame.init()

rez=(1280,720)
screen=pygame.display.set_mode(rez)
box1=pygame.Rect(10,10,10,80)
box2=pygame.Rect(1260,10,10,80)
ball=pygame.Rect(637,357,6,6)

b_spin=1
rpion=b_spin
rpoz=b_spin
max_tps=120
odb=0
dt=0.0

clock=pygame.time.Clock()
delta = 0.0

while True:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    # TICKING
    delta += clock.tick()/1000.0

    while delta > 1/max_tps:

    # INPUT
        if pygame.key.get_pressed() [pygame.K_s]:
            if box1.y + box1.height < rez[1]:
                box1.y += 4
        if pygame.key.get_pressed() [pygame.K_w]:
            if box1.y >0:
                box1.y -= 4

        if pygame.key.get_pressed() [pygame.K_DOWN]:
            if box2.y + box2.height < rez[1]:
                box2.y += 4
        if pygame.key.get_pressed() [pygame.K_UP]:
            if box2.y >0:
                box2.y -= 4


        # odbicia pilki

        # sufit i podloga
        if ball.y +ball.height > rez[1]:
            rpion= -b_spin
            if rpoz < 0:
                rpoz = -b_spin
            else:
                rpoz = b_spin
        if ball.y < 0:
            rpion= b_spin
            if rpoz < 0:
                rpoz = -b_spin
            else:
                rpoz = b_spin

        # paletka 2
        if box2.x <= ball.x + ball.width:
            if ball.y < box2.y + box2.height and ball.y + ball.height > box2.y:
                rpoz= -b_spin

        # paletka 1
        if box1.x + box1.width >= ball.x:
            if ball.y < box1.y + box1.height and ball.y + ball.height > box1.y:
                rpoz= b_spin


        # pilka movement
        ball.x +=rpoz
        ball.y +=rpion
        if b_spin < 10:
            odb += 1
            if odb > 600:
                b_spin += 1
                odb = 0
        delta = 0



    if ball.x < 0 or ball.x + ball.width > 1280:
        break

    # Drawing
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,150,255), box1)
    pygame.draw.rect(screen, (255, 15, 0), box2)
    pygame.draw.rect(screen, (15, 255, 15), ball)
    pygame.display.flip()


# Press the green button in the gutter to run the script.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/