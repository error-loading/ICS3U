import pygame

GREEN = (0, 255, 0)


WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
        mx, my = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()

    for i in range(-900, 900, 10):
        pygame.draw.line(screen, GREEN, (i, 0), (i+750, 800), 1)
        pygame.draw.line(screen, GREEN, (900 - i, 0), (900 - i-750, 800), 1)
    pygame.display.flip()

pygame.quit()
