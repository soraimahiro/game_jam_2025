import pygame
from canvas import Canvas

while True:
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Window")
    background_color = (0, 0, 0)  # Black background
    canvas = Canvas(background_color)
    canvas.draw_background(screen)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            pass
    




