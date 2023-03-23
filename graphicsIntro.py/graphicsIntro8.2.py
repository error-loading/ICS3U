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
    
    for i in range(10, 150, 10):
        pygame.draw.line(screen, (0, 255, 0), (WIDTH/2-2*i, HEIGHT/2-2*i), (WIDTH/2-2*i, HEIGHT/2+2*i))
        pygame.draw.line(screen, (0, 255, 0), (WIDTH/2-2*i, HEIGHT/2-2*i), (WIDTH/2+2*i, HEIGHT/2-2*i))
        pygame.draw.line(screen, (0, 255, 0), (WIDTH/2+2*i, HEIGHT/2-2*i), (WIDTH/2+2*i, HEIGHT/2+2*i+20))
        pygame.draw.line(screen, (0, 255, 0), (WIDTH/2+2*i, HEIGHT/2+2*i+20), (WIDTH/2-2*i-20, HEIGHT/2+2*i+20))
    
    pygame.display.flip()

pygame.quit()