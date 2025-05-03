import pygame
from vector2 import Vector2
from skill import Skill
import globals

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.pos = Vector2(0, 0)
		self.icon = pygame.transform.scale(globals.player_icon, (50, 50))
		self.money = 0
		self.hp = 10
		self.killed = 0
		self.skills = [Skill(1, 3, 0)] # 預設為射程3傷害1的十字攻擊
		pass
	def attack(self, entity):
		if entity.hp <= 0:
			return
		for skill in self.skills:
			if skill.direction == 0:
				if entity.pos.y == self.pos.y and entity.pos.x >= self.pos.x - skill.range and entity.pos.x <= self.pos.x + skill.range:
					entity.hp -= skill.damage
					skill.hit_enemy(entity.pos, pygame.time.get_ticks())
					print (f"entity hp = {entity.hp}")
				elif entity.pos.x == self.pos.x and entity.pos.y >= self.pos.y - skill.range and entity.pos.y <= self.pos.y + skill.range:
					entity.hp -= skill.damage
					skill.hit_enemy(entity.pos, pygame.time.get_ticks())
					print (f"entity hp = {entity.hp}")
		if entity.hp <= 0:
			self.killed += 1
			self.money += entity.value
			# print (f"money = {self.money}")