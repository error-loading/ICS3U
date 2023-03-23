import pygame
from random import randint

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    col = (randint(0, 255), randint(0, 255), randint(0, 255))
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()

    if mb[0]:
        dist = ((mx - WIDTH/2)**2 + (my - HEIGHT/2) ** 2) ** 0.5
        pygame.draw.circle(screen, col, (mx, my), dist/10)
    elif mb[2]:
        screen.fill((0, 0, 0))

    pygame.display.flip()

pygame.quit()