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
    for i in range(-600, 600, 10):
        for j in range(60, 600, 10):
            pygame.draw.circle(screen, (0, 255, 0),
                               ((i + WIDTH/2), 0.0035*(i)**2 + j), 4)

    pygame.display.flip()

pygame.quit()
