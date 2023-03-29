import pygame
from random import randint

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((100, 0, 0))

running = True

arr = []

pressed = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()
    screen.fill((255, 200, 200))

    for x, y in arr:
        pos = (x, y)
        pygame.draw.circle(screen, (200, 200, 255), pos, 15)

    if mb[0]:
        pygame.draw.circle(screen, (200, 200, 255), (mx, my), 15)
        pressed = True
    elif pressed:
        pos = (mx, my)
        arr.append(pos)
        pressed = False



    pygame.display.flip()

pygame.quit()
