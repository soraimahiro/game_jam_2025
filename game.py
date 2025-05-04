import pygame
from stage import Stage, StageOption, TitleOption
from canvas import draw
from pressed import pressed
import globals
import os

pygame.init()
pygame.display.set_caption("Shadow maze")
screen = pygame.display.set_mode((800, 600))
globals.init()
clock = pygame.time.Clock()
stage = Stage()
stage.set_stage(StageOption.TITLE)

while True:
	clock.tick(60)
	draw(stage, screen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(1)
		elif event.type == pygame.KEYDOWN:
			if not pressed(stage, event.key):
				pygame.quit()
				exit(1)
			pass
	pygame.display.flip()
	
	




