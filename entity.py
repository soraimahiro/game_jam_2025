# entity.py
import pygame
import random
from vector2 import Vector2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from player import Player

class Entity(pygame.sprite.Sprite):
	T_MOSTER = 0;	T_BOSS = 1;	T_SHADOW = 2;	T_SHOP = 3; T_HIT = 4
	def __init__(self, icon: str, type: int, hp: int, damage: int, pos: Vector2, mov: Vector2, value: int = 1, wait_time: int = 1):
		super().__init__()
		self.type = type  # type of entity
		self.hp = hp
		self.damage = damage
		self.pos = pos
		self.icon = pygame.transform.scale(pygame.image.load(icon), (75, 75))
		self.move = mov # how long do the entity move
		self.wait_time = wait_time  # how many rounds do the entity take to move
		self.round_pass = 0  # how many rounds pass
		self.value = value
	def __repr__(self):
		return f"Entity type {self.type} at {self.pos}"
	def next_step(self, player : 'Player'): # pass to next position 
		if self.type == Entity.T_MOSTER:
			if self.pos.x < -6 or self.pos.x > 6 or self.pos.y < -4 or self.pos.y > 4:
				self.hp = 0
		elif self.type == Entity.T_BOSS:
			sight = player.pos - self.pos
			better = self.move
			most_dot = self.move * sight
			possible = Vector2(-self.move.x, self.move.y)
			if possible * sight > most_dot:
				better = Vector2(possible.x, possible.y)
			possible = Vector2(self.move.x, -self.move.y)
			if possible * sight > most_dot:
				better = Vector2(possible.x, possible.y)
			possible = Vector2(-self.move.x, -self.move.y)
			if possible * sight > most_dot:
				better = Vector2(possible.x, possible.y)
			possible = Vector2(self.move.y, self.move.x)
			if possible * sight > most_dot:
				better = Vector2(possible.x, possible.y)
			possible = Vector2(-self.move.y, self.move.x)
			if possible * sight > most_dot:
				better = Vector2(possible.x, possible.y)
			possible = Vector2(self.move.y, -self.move.x)
			if possible * sight > most_dot:
				better = Vector2(possible.x, possible.y)
			possible = Vector2(-self.move.y, -self.move.x)
			if possible * sight > most_dot:
				better = Vector2(possible.x, possible.y)
			self.move = better
		self.round_pass += 1
		if self.round_pass >= self.wait_time:
			self.pos.x += self.move.x
			self.pos.y += self.move.y
			self.round_pass -= self.wait_time
		pass
	@ classmethod
	def random_enemy(self):
		rx = random.choice((-1, 1))
		ry = random.randrange(-3, 4)
		return Entity("./resource/image/iron_ingot.png", Entity.T_MOSTER, 1, 1, Vector2(rx * -6, ry), Vector2(rx, 0))
	@ classmethod
	def random_boss(self):
		rx = random.choice((-1, 1))
		ry = random.choice((-1, 1))
		return Entity("./resource/image/lava_bucket.png", Entity.T_BOSS, 10, 2, Vector2(rx * -6, ry * -4), Vector2(1, 1), 10, 3)
	@ classmethod
	def shadow(self, pos: Vector2):
		return Entity("./resource/image/emerald.png", Entity.T_SHADOW, -1, 0, pos, Vector2(0, 0))