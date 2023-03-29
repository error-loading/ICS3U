import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((111, 255, 111))

    mx, my = pygame.mouse.get_pos()

    for i in range(0, WIDTH+100, 25):
        for j in range(0, HEIGHT+100, 25):
            dist = ((my-j)**2 + (mx-i)**2)**0.5
            pygame.draw.circle(screen, (111, 111, 111), (i, j), dist//40)


    pygame.display.flip()

pygame.quit()
