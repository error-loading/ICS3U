import pygame
from math import sin, cos, radians

screen = pygame.display.set_mode((800, 600))

running = True

def star(x, y, sz, col):
    wdth = sz * cos(radians(72))
    hgt = sz * sin(radians(72))

    shrtWdth = sz * cos(radians(36))
    shrtHgt = sz * sin(radians(36))

    mdWdth = sz * cos(radians(36))
    mdHgt = sz * sin(radians(36))

    pygame.draw.line(screen, col, (x, y), (x + shrtWdth, y - shrtHgt))

    ox, oy = x + shrtWdth, y - shrtHgt
    pygame.draw.line(screen, col, (ox, oy), (ox + shrtWdth, oy + shrtHgt))

    ox, oy = ox + shrtWdth, oy + shrtHgt
    pygame.draw.line(screen, col, (ox, oy), (ox - wdth, oy - hgt))

    ox, oy = ox - wdth, oy - hgt
    pygame.draw.line(screen, col, (ox, oy), (ox + mdWdth, oy - mdHgt))

    ox, oy = ox + mdWdth, oy - mdHgt
    pygame.draw.line(screen, col, (ox, oy), (ox - sz, oy))

    ox, oy = ox - sz, oy
    pygame.draw.line(screen, col, (ox, oy), (ox - wdth, oy - hgt))

    ox, oy = ox - wdth, oy - hgt
    pygame.draw.line(screen, col, (ox, oy), (ox - wdth, oy + hgt))

    ox, oy = ox - wdth, oy + hgt
    pygame.draw.line(screen, col, (ox, oy), (ox - sz, oy))

    ox, oy = ox - sz, oy
    pygame.draw.line(screen, col, (ox, oy), (ox + mdWdth, oy + mdHgt))

    ox, oy = ox + mdWdth, oy + mdHgt
    pygame.draw.line(screen, col, (ox, oy), (x, y))

while running:
    star(400, 300, 100, (255, 0, 0))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.QUIT()
