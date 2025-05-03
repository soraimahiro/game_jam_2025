import pygame
from stage import Stage, StageOption, TitleOption
from canvas import draw
from pressed import pressed
import globals

pygame.init()
globals.init()
pygame.display.set_caption("Game Window")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
stage = Stage()
stage.set_stage(StageOption.TITLE)


while True:
	clock.tick(60)
	draw(stage, screen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN:
			if not pressed(stage, event.key):
				pygame.quit()
				exit()
			pass
	pygame.display.flip()
	
	




