import pygame
from math import sin, cos, radians
from random import *

import datetime

def clock(hr, min, sec):
    pygame.draw.circle(screen, (255, 255, 255), (400, 300), 100)

    for rot in range(12):
        first = cos(radians(30 + 30 * rot))
        second = sin(radians(30 + 30 * rot))

        pygame.draw.line(screen, 0, (400 + 80 * first, 300 + 80 * second), (400 + 95 * first, 300 + 95 * second))

    hrAng = radians(30 * (hr - 3))
    pygame.draw.line(screen, (0, 255, 0), (400, 300), (400 + 50 * cos(hrAng), 300 + 50 * sin(hrAng)))

    minAng = radians(30 * (min / 5 - 3))
    pygame.draw.line(screen, (0, 255, 0), (400, 300), (400 + 75 * cos(minAng), 300 + 75 * sin(minAng)))

    secAng = radians(30 * (sec / 5 - 3))
    pygame.draw.line(screen, (0, 0, 0), (400, 300), (400 + 75 * cos(secAng), 300 + 75 * sin(secAng)))


screen = pygame.display.set_mode((1000,750))

running =True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    screen.fill(0)
    now = datetime.datetime.now()
    clock((now.hour-1)%12+1, now.minute, now.second)
    pygame.display.flip()
    pygame.time.wait(20)


quit()
