import pygame
from vector2 import Vector2
from skill import Skill
import globals
from skill import AttackType
import random
import os

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.pos = Vector2(0, 0)
		self.icon = pygame.transform.scale(globals.player_icon, (50, 50))
		self.money = 0
		self.hp = 10
		self.killed = 0
		self.skills = [Skill(1, 3, 3)] # 預設為射程3傷害1的十字攻擊
		pass
	def attack(self, entity):
		if entity.hp <= 0:
			return
		for skill in self.skills:
			if skill.attacktype == AttackType.POINT.value:
				#待實作
				pass
			elif skill.attacktype == AttackType.LINE_X.value:
				if entity.pos.y == self.pos.y:
					if entity.pos.x >= self.pos.x - skill.level and entity.pos.x <= self.pos.x + skill.level:
						entity.hp -= skill.damage
						skill.hit_enemy(entity.pos, pygame.time.get_ticks())
						print (f"entity hp = {entity.hp}")
			elif skill.attacktype == AttackType.LINE_Y.value:
				if entity.pos.x == self.pos.x:
					if entity.pos.y >= self.pos.y - skill.level and entity.pos.y <= self.pos.y + skill.level:
						entity.hp -= skill.damage
						skill.hit_enemy(entity.pos, pygame.time.get_ticks())
						print (f"entity hp = {entity.hp}")
			elif skill.attacktype == AttackType.LINE_XY.value:
				if entity.pos.y == self.pos.y and entity.pos.x >= self.pos.x - skill.level and entity.pos.x <= self.pos.x + skill.level:
					entity.hp -= skill.damage
					skill.hit_enemy(entity.pos, pygame.time.get_ticks())
					print (f"entity hp = {entity.hp}")
				elif entity.pos.x == self.pos.x and entity.pos.y >= self.pos.y - skill.level and entity.pos.y <= self.pos.y + skill.level:
					entity.hp -= skill.damage
					skill.hit_enemy(entity.pos, pygame.time.get_ticks())
					print (f"entity hp = {entity.hp}")
			elif skill.attacktype == AttackType.AREA.value:
				if entity.pos.x >= self.pos.x - skill.level and entity.pos.x <= self.pos.x + skill.level and entity.pos.y >= self.pos.y - skill.level and entity.pos.y <= self.pos.y + skill.level:
					entity.hp -= skill.damage
					skill.hit_enemy(entity.pos, pygame.time.get_ticks())
					print (f"entity hp = {entity.hp}")
				pass
		if entity.hp <= 0:
			self.killed += 1
			self.money += entity.value
			# print (f"money = {self.money}")