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
	def __repr__(self):
		return f"Entity type {self.type} at {self.pos}"
	def next_step(self): # pass to next position 
		self.round_pass += 1
		if self.round_pass >= self.wait_time:
			self.pos.x += self.move.x
			self.pos.y += self.move.y
			self.round_pass -= self.wait_time
		if self.type == Entity.T_MOSTER:
			if self.pos.x < -5 or self.pos.x > 5 or self.pos.y < -3 or self.pos.y > 3:
				self.hp = 0
		pass
	@ classmethod
	def random_enemy(self):
		rx = random.choice((-1, 1))
		ry = random.randrange(-3, 4)
		return Entity("./resource/image/iron_ingot.png", Entity.T_MOSTER, 1, Vector2(rx * -5, ry), Vector2(rx, 0))
	@ classmethod
	def shadow(self, pos: Vector2):
		return Entity("./resource/image/emerald.png", Entity.T_SHADOW, -1, pos, Vector2(0, 0))