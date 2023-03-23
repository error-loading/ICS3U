import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        mx, my = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()
        if mb[0]:
            screen.fill((0, 0, 0))
            pygame.draw.line(screen, (255, 0, 0), (mx, 0), (mx, HEIGHT))
            pygame.draw.line(screen, (255, 0, 0), (0, my), (WIDTH, my))

    pygame.display.flip()

pygame.quit()