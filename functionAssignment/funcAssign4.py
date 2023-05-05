import pygame

screen = pygame.display.set_mode((800, 600))
running = True

def grid(x, y, width, height, spacing, col):
    for i in range(x, x + width + 1, spacing):
        pygame.draw.line(screen, col, (i, y), (i, y + height))

    for i in range(y, y + height + 1, spacing):
        pygame.draw.line(screen, col, (x, i), (x + width, i))
    

while running:
    grid(100, 100, 150, 50, 10, (0, 255, 0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()