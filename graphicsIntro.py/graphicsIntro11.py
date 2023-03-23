import pygame
from random import randint

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((100, 0, 0))

running = True

arr = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()



    if mb[0]:
        while not mb[0]:
            screen.fill((100, 0, 0))
            mx, my = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0, 0, 255), (mx, my), 5)
        arr.append((mx, my))

    for x, y in arr:
        pygame.draw.circle(screen, (0, 0, 255), (x, y), 5)


    pygame.display.flip()

pygame.quit()
