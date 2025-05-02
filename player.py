import pygame
from vector2 import Vector2
from skill import Skill

# Player(x, y, width, height)
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.pos = Vector2(0, 0)
		self.icon = pygame.transform.scale(
			pygame.image.load("./resource/image/diamond.png"),
			(100, 100)
		)
		self.rect = self.icon.get_rect()
		self.money = 0
		self.hp = 100
		self.skills = []
		pass
