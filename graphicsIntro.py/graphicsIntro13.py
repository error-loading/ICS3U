import pygame

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
    for y in range(10, HEIGHT, 20):
        for x in range(0, WIDTH, 20):
            temp = y
            for y2 in range(y, y-10, -1):
                screen.fill((0, 0, 0))
                pygame.draw.line(screen, (0, 255, 0), (x, y), (x+10, y2))
                pygame.draw.line(screen, (0, 255, 0), (x+10, y2), (x+20, y))


    pygame.display.flip()

pygame.quit()
