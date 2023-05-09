'''
Gurjas Dhillon
funcAssign5.py
create a star using math/trig
'''

import pygame
from math import sin, cos, radians

screen = pygame.display.set_mode((800, 600))

running = True

def star(x, y, sz, col):
    # width and height of a right angle with an angle of 72
    wdth = sz * cos(radians(72))
    hgt = sz * sin(radians(72))

    # width and height of a right angle with an angle of 36
    shrtWdth = sz * cos(radians(36))
    shrtHgt = sz * sin(radians(36))


    # bottom left to bottom middle (right triangle with angle 36)
    pygame.draw.line(screen, col, (x, y), (x + shrtWdth, y - shrtHgt))

    # bottom middle to bottom right (right triangle with angle 36)
    ox, oy = x + shrtWdth, y - shrtHgt
    pygame.draw.line(screen, col, (ox, oy), (ox + shrtWdth, oy + shrtHgt))

    # bottom right to middle right (right triangle with angle 72)
    ox, oy = ox + shrtWdth, oy + shrtHgt
    pygame.draw.line(screen, col, (ox, oy), (ox - wdth, oy - hgt))

    # middle right to top right (right triangle with angle 36)
    ox, oy = ox - wdth, oy - hgt
    pygame.draw.line(screen, col, (ox, oy), (ox + shrtWdth, oy - shrtHgt))

    # top right to the top-middle-right (horizontal line)
    ox, oy = ox + shrtWdth, oy - shrtHgt
    pygame.draw.line(screen, col, (ox, oy), (ox - sz, oy))

    # top-middle right to the highest point (right triangle with angle 72)
    ox, oy = ox - sz, oy
    pygame.draw.line(screen, col, (ox, oy), (ox - wdth, oy - hgt))

    # highest point to the top-middle left  (right triangle with angle 72)
    ox, oy = ox - wdth, oy - hgt
    pygame.draw.line(screen, col, (ox, oy), (ox - wdth, oy + hgt))

    # top middle left to top left (horizontal line)
    ox, oy = ox - wdth, oy + hgt
    pygame.draw.line(screen, col, (ox, oy), (ox - sz, oy))

    # top left to middle left (right triangle with angle 36)
    ox, oy = ox - sz, oy
    pygame.draw.line(screen, col, (ox, oy), (ox + shrtWdth, oy + shrtHgt))

    # middle left returning back to starting point
    ox, oy = ox + shrtWdth, oy + shrtHgt
    pygame.draw.line(screen, col, (ox, oy), (x, y))

while running:
    star(400, 300, 100, (255, 0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.QUIT()
