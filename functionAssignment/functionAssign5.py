import pygame
from math import sin, cos, radians

screen = pygame.display.set_mode((800, 600))

running = True

def trig(x, y, sz, angle1):
    wid = sz * cos(radians(angle1))

    hei = sz * sin(radians(angle1))

    print(wid, hei)

    return (wid, hei)


def star(x, y, size, col):
    pygame.draw.line()


star(100, 150, 50, (255, 0, 0))

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.QUIT()
