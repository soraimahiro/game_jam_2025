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
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				canvas = Canvas()
			elif event.key in {pygame.K_w, pygame.K_UP}:
				if canvas.player.pos.y > -3:
					canvas.player.pos.y -= 1
					canvas.next_round()
			elif event.key in {pygame.K_s, pygame.K_DOWN}:
				if canvas.player.pos.y < 3:
					canvas.player.pos.y += 1
					canvas.next_round()
			elif event.key in {pygame.K_a, pygame.K_LEFT}:
				if (canvas.player.pos.x > -5):
					canvas.player.pos.x -= 1
					canvas.next_round()
			elif event.key in {pygame.K_d, pygame.K_RIGHT}:
				if (canvas.player.pos.x < 5):
					canvas.player.pos.x += 1
					canvas.next_round()
			pass
	
	




