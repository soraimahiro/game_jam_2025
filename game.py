import pygame
import os
from canvas import Canvas

pygame.init()
pygame.display.set_caption("Game Window")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
canvas = Canvas()
while True:
	clock.tick(60)
	canvas.draw(screen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				canvas = Canvas()
			if not canvas.pressed(event.key):
				pygame.quit()
				exit()
			pass
	pygame.display.flip()
	
	




