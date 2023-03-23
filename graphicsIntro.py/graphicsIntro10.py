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
    screen.fill((0, 0, 0))
    mx, my = pygame.mouse.get_pos()

    for i in range(0, 11):
        pygame.draw.line(screen, (0, 255, 0), (i*WIDTH//11, 0), (mx-40+ i*80/11, my - 40))
        pygame.draw.line(screen, (0, 255, 0), (i*WIDTH//11, HEIGHT), (mx-40+ i*80/11, my + 40))
        pygame.draw.line(screen, (0, 255, 0), (0, i*HEIGHT//11), (mx-40, my - 40+ i*80/11))
        pygame.draw.line(screen, (0, 255, 0), (WIDTH, i*HEIGHT//11), (mx+40, my - 40+ i*80/11))

    pygame.display.flip()

pygame.quit()
