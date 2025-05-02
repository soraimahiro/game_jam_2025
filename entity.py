# entity.py
import pygame
import random
from vector2 import Vector2 

class Entity(pygame.sprite.Sprite):
	T_MOSTER = 0;	T_BOSS = 1;	T_SHADOW = 2;	T_SHOP = 3
	def __init__(self, icon: str, type: int, hp: int, pos: Vector2, mov: Vector2, wait_time: int = 1):
		super().__init__()
		self.type = type  # type of entity
		self.hp = hp
		self.pos = pos
		self.icon = pygame.transform.scale(pygame.image.load(icon), (100, 100))
		self.move = mov # how long do the entity move
		self.wait_time = wait_time  # how many rounds do the entity take to move
		self.round_pass = 0  # how many rounds pass
	def next_step(self): # pass to next position 
		self.round_pass += 1
		if self.round_pass >= self.wait_time:
			self.pos.x += self.move.x
			self.pos.y += self.move.y
			self.round_pass -= self.wait_time
		pass
