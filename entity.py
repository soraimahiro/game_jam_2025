# entity.py
import pygame
import random
from vector2 import Vector2 

class Entity(pygame.sprite.Sprite):
	def __init__(self):
		self.type = 0  # type of entity
		self.pos = Vector2(random.randrange(-5, 5), random.randrange(-3, 3))
		self.icon = pygame.transform.scale(
			pygame.image.load("./resource/image/iron_ingot.png"),
			(100, 100)
		)
		self.hp = 0
		self.x_move_amount = 0  # how long do the entity move
		self.y_move_amount = 0  # only boss has this
		self.wait_time = 0  # how many rounds do the entity take to move
		self.round_pass = 0  # how many rounds pass
		def next_step(self): # pass to next position 
			self.round_pass += 1
			if self.round_pass >= self.wait_time:
				self.pos.x += self.x_move_amount
				self.pos.y += self.y_move_amount
		def draw(self, screen: pygame.Surface, x: int, y: int):
			screen.blit(self.icon, (x, y))
			pass
