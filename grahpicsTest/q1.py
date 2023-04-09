import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

screen.fill((255, 255, 255))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()
    if mb[0]:
        for i in range(5, 46, 5):
            pygame.draw.circle(screen, (255, 0, 0), (mx, my), i, 1)
    


    pygame.display.flip()

pygame.quit()
