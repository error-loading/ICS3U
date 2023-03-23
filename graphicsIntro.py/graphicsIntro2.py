import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

GREEN = (0, 255, 0)

while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False
        
        mx, my = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()

        if mb[0]:
            
            for i in range(-20, 30, 10):
                pygame.draw.circle(screen, GREEN, (mx + i, my - 20), 4, 20)
                pygame.draw.circle(screen, GREEN, (mx + i, my + 20), 4, 20)
                pygame.draw.circle(screen, GREEN, (mx - 20, my + i), 4, 20)
                pygame.draw.circle(screen, GREEN, (mx + 20, my + i), 4, 20)
                # pygame.draw.circle(screen, GREEN, (mx - i + 10, my + 10), 10, 2)
            
            pygame.display.flip()

pygame.quit()