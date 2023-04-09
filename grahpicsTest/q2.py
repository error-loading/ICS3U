import pygame
from random import randint

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True


col = []

for i in range(20):
    col.append((randint(0, 255), randint(0,255), randint(0,255)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()

    if mb[0]:
        endPt = (mx+randint(-30, 30), my + randint(-30, 30))
        i = mx//40
        pygame.draw.line(screen, col[i], (mx, my), endPt)
    if mb[2]:
        screen.fill(0)

    for x in range(20):
        pygame.draw.rect(screen, col[x], (40*x,290,40,40))


    pygame.display.flip()

pygame.quit()
