import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))

    mx, my = pygame.mouse.get_pos()

    for i in range(1, WIDTH, 25):
        for j in range(1, HEIGHT, 25):
            dist = ((my-j)**2 + (mx-i)**2)**0.5

            if dist == 0:
                pass
            else:
                pygame.draw.line(screen, (0, 0, 0), (i, j), (i+(mx-i)*10//dist, j+(my-j)*10//dist))

            pygame.draw.circle(screen, (255, 0, 0), (i, j), 3)


    pygame.display.flip()

pygame.quit()
