import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True

box = [0 for i in range(30)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mx, my = pygame.mouse.get_pos()
    mb = pygame.mouse.get_pressed()

    if mb[0]: mcol = 2
    elif mb[2]: mcol = 1
    else: mcol = 0


    if 300 < my < 300 + WIDTH//30:
        i = mx // 30
        box[i] = mcol
    pygame.draw.circle(screen, mcol, (mx, my), 3)
    
    screen.fill((255, 255, 255))
    for i in range(0, WIDTH, WIDTH//30):
        col = box[i % WIDTH//30]
        if col == 0:
            pygame.draw.rect(screen, (255, 255, 255), (i, 300, WIDTH//30, WIDTH//30))
            pygame.draw.rect(screen, (0, 0, 0), (i, 300, WIDTH//30, WIDTH//30), 1)
        elif col == 1:
            pygame.draw.rect(screen, (255, 0, 0), (i, 300, WIDTH//30, WIDTH//30))
            pygame.draw.rect(screen, (0, 0, 0), (i, 300, WIDTH//30, WIDTH//30), 1)
        elif col == 2:
            pygame.draw.rect(screen, (0, 255, 0), (i, 300, WIDTH//30, WIDTH//30))
            pygame.draw.rect(screen, (0, 0, 0), (i, 300, WIDTH//30, WIDTH//30), 1)
    box=[box[-1]] + box[:-1]
    pygame.time.wait(60)
    


    pygame.display.flip()

pygame.quit()
