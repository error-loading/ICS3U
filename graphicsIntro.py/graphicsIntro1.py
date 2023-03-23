import pygame

screen = pygame.display.set_mode((800,600))

running =True
while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

        mx, my = pygame.mouse.get_pos()
        mb = pygame.mouse.get_pressed()
        if mb[0]:
            pygame.draw.line(screen, (255, 0, 0), (mx - 25, my - 25), (mx + 25, my + 25), 3)
            pygame.draw.line(screen, (255, 0, 0, 0), (mx + 25, my - 25), (mx - 25, my + 25), 3)

        elif mb[2]:
            pygame.draw.circle(screen, (0, 255, 0), (mx, my), 25, 2)
            
    pygame.display.flip()

pygame.quit()