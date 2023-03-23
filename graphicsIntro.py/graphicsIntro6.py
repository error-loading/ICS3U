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
        mx, my = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()
        if mb[0]:
            col = (randint(0, 255), randint(0, 255), randint(0, 255))
            if mx <= WIDTH / 2 and my <= HEIGHT / 2:
                pygame.draw.line(screen, col, (0, 0), (mx, my))
            elif mx > WIDTH / 2 and my <= HEIGHT / 2:
                pygame.draw.line(screen, col, (WIDTH, 0), (mx, my))
            elif mx <= WIDTH / 2 and my > HEIGHT / 2:
                pygame.draw.line(screen, col, (0, HEIGHT), (mx, my))
            else:
                pygame.draw.line(screen, col, (WIDTH, HEIGHT), (mx, my))

    pygame.display.flip()

pygame.quit()