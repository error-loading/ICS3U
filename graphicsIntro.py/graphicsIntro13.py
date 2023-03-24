import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

clock = pygame.time.Clock()
fps = 10

thingY = 0
inc = 1

while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))

    mx, my = pygame.mouse.get_pos()

    for y in range(20, HEIGHT, 20):
        for x in range(0, WIDTH, 20):
            pygame.draw.line(screen, (0, 255, 0), (x, y), (x+10, y-thingY))
            pygame.draw.line(screen, (0, 255, 0), (x+10, y-thingY), (x+20, y))

    if thingY == 10 or thingY == -10:
        inc *= -1
    
    thingY += inc

    pygame.display.flip()

pygame.quit()
