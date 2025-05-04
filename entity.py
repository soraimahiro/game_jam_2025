# entity.py
import pygame
import random
import globals
from vector2 import Vector2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from player import Player

class Entity(pygame.sprite.Sprite):
	T_MONSTER = 0;	T_BOSS = 1;		T_SHADOW = 2;	T_SHOP = 3;	T_HIT = 4
	T_REGEN = 7
	
	def __init__(self, img: str, type: int, hp: int, damage: int, pos: Vector2, mov: Vector2, value: int = 1, wait_time: int = 1, direction: int = 0b0000):
		super().__init__()
		self.type = type  # type of entity
		self.hp = hp
		self.damage = damage
		self.pos = pos
		self.pre_pos = pos.copy()
		self.img = img
		self.img_alpha = 255
		self.move = mov # how long do the entity move
		self.wait_time = wait_time  # how many rounds do the entity take to move
		self.round_pass = 0  # how many rounds pass
		self.value = value
		self.direction = direction # 0b 0 0 0 0 -> 0b up down left right
	
	def copy(self):
		return Entity(self.img, self.type, self.hp, self.damage, self.pos, self.move, self.value, self.wait_time, self.direction)
	
	def icon(self):
		if self.direction != 0b0000:
			direction: dict[int, int | float] = {}
			if (self.direction & 0b1000) != 0: # moving up
				direction[0b1000] = self.move * Vector2(0, -1)
			if (self.direction & 0b0100) != 0: # moving down
				direction[0b0100] = self.move * Vector2(0, 1)
			if (self.direction & 0b0010) != 0: # moving left
				direction[0b0010] = self.move * Vector2(-1, 0)
			if (self.direction & 0b0001) != 0: # moving right
				direction[0b0001] = self.move * Vector2(1, 0)
			maxat = 0b0000
			if direction.keys():
				maxat = max(direction.keys(), key= lambda k : direction.get(k))
			if maxat == 0b1000:
				icon = globals.icon(f"./resource/image/{self.img}_up.png")
			elif maxat == 0b0100:
				icon = globals.icon(f"./resource/image/{self.img}_down.png")
			elif maxat == 0b0010:
				icon = globals.icon(f"./resource/image/{self.img}_left.png")
			else: # maxat == 0b0001
				icon = globals.icon(f"./resource/image/{self.img}_right.png")
		elif self.type == Entity.T_SHADOW:
			icon = globals.icon(f"./resource/image/{globals.get_shadow_img()}.png", (40, 40))
		else:
			icon = globals.icon(f"./resource/image/{self.img}.png")
		icon.set_alpha(self.img_alpha)
		return icon
	
	def __repr__(self):
		return f"Entity {self.img} type {self.type} at {self.pos}"
	
	def next_step(self, player : 'Player'): # pass to next position 
		#print("next_step")
		if self.type == Entity.T_MONSTER:
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
	def random_enemy(self, boss: bool, lvl: int = 0):
		if lvl not in range(1, 5):
			return ENEMIES[1][0].copy()
		choice: Entity = ENEMIES[lvl][0].copy()
		#print(choice.img)
		if boss and random.choice((True, False)) and (choice.direction == 0 or (choice.direction | 0b1100) != 0):
			rx = random.randint(-5, 5)
			ry = random.choice((-3, 3))
			#print("here")
			if ry == 3: # up type
				choice.move = Vector2(choice.move.y, -choice.move.x)
			else: # down type
				choice.move = Vector2(choice.move.y, choice.move.x)
		else:
			rx = random.choice((-5, 5))
			ry = random.randint(-3, 3)
			if rx == 5: # left type
				choice.move = Vector2(-choice.move.x, choice.move.y)
		choice.pos = Vector2(rx, ry)
		return choice
	
	@ classmethod
	def random_boss(self, lvl: int = 0):
		if lvl not in range(1, 5):
			return ENEMIES[1][1].copy()
		choice: Entity = ENEMIES[lvl][0].copy()
		#print(choice.img)
		if random.choice((True, False)):
			rx = random.randint(-5, 5)
			ry = random.choice((-3, 3))
			if ry == 3: # up type
				choice.move = Vector2(choice.move.y, -choice.move.x)
			else: # down type
				choice.move = Vector2(choice.move.y, choice.move.x)
		else:
			rx = random.choice((-5, 5))
			ry = random.randint(-3, 3)
			if rx == 5: # left type
				choice.move = Vector2(-choice.move.x, choice.move.y)
		choice.pos = Vector2(rx, ry)
		choice.type = Entity.T_BOSS
		return choice
	
	@ classmethod
	def shadow(self, pos: Vector2):
		return Entity(globals.shadow_img, Entity.T_SHADOW, 100000, 0, pos, Vector2(0, 0))

ENEMIES = {
	1: (
		Entity("type_jam/image_mob_move",			Entity.T_MONSTER,	1,	1,	Vector2(0, 0),	Vector2(1, 0),	1,	2,	0b0011),
		Entity("type_jam/image_boss_move",			Entity.T_BOSS,		10,	2,	Vector2(0, 0),	Vector2(1, 1),	10,	2,	0b0011)
	),
	2: (
		Entity("type_simple/image_mob_move",		Entity.T_MONSTER,	1,	1,	Vector2(0, 0),	Vector2(1, 0),	2,	1,	0b1111),
		Entity("type_simple/image_boss_move",		Entity.T_MONSTER,	10,	2,	Vector2(0, 0),	Vector2(2, 0),	10,	3,	0b1111)
	),
	3: (
		Entity("element/element",					Entity.T_MONSTER,	2,	1,	Vector2(0, 0),	Vector2(1, 0),	3,	2,	0b1111),
		Entity("element/boss",						Entity.T_BOSS,		10,	2,	Vector2(0, 0),	Vector2(2, 2),	10,	2,	0b1111)
	),
	4: (
		Entity("monsters/image_monster2_mob_move",	Entity.T_BOSS,		2,	1,	Vector2(0, 0),	Vector2(1, 0),	4,	1,	0b0011),
		Entity("monsters/image_monster2_boss_move",	Entity.T_BOSS,		10,	3,	Vector2(0, 0),	Vector2(2, 1),	10,	2,	0b0011)
	)
}