import pygame
from vector2 import Vector2
from skill import Skill
import globals
from skill import AttackType
import random
import os
from setting import Setting
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from entity import Entity
# Player(x, y, width, height)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.pos = Vector2(0, 0)
		self.money = 0
		self.hp = 10
		self.killed = 0
		self.skills = [Skill(1, 3, 3)] # 預設為射程3傷害1的十字攻擊
		pass
	def attack(self, entities: list):
		attackdata = set()
		MAX_X=5
		MAX_Y=3
		for skill in self.skills:
			if skill.attacktype == AttackType.POINT.value:
				# 隨機 n 個位置
				for i in range(skill.level):
					x = random.randint(-MAX_X, MAX_X)
					y = random.randint(-MAX_Y, MAX_Y)
					attackdata.add((Vector2(x, y), skill.damage))
			elif skill.attacktype == AttackType.LINE_X.value:
				# x方向；以角色位置為參考點，x方向距離 n 單位內的敵人受傷害 X
				for x in range(self.pos.x - skill.level, self.pos.x + skill.level + 1):
					if x < -MAX_X or x > MAX_X:
						continue
					attackdata.add((Vector2(x, self.pos.y), skill.damage))
			elif skill.attacktype == AttackType.LINE_Y.value:
				# y方向；以角色位置為參考點，y方向距離 n 單位內的敵人受傷害 X
				for y in range(self.pos.y - skill.level, self.pos.y + skill.level + 1):
					if y < -MAX_Y or y > MAX_Y:
						continue
					attackdata.add((Vector2(self.pos.x, y), skill.damage))
			elif skill.attacktype == AttackType.LINE_XY.value:
				# xy方向;以角色位置為參考點，xy方向距離 n 單位內的敵人受傷害 X
				
				for x in range(self.pos.x - skill.level, self.pos.x + skill.level + 1):
					if x < -MAX_X or x > MAX_X:
						continue
					attackdata.add((Vector2(x, self.pos.y), skill.damage))
				# print(f"attackdata = {attackdata}")
				for y in range(self.pos.y - skill.level, self.pos.y + skill.level + 1):
					if y < -MAX_Y or y > MAX_Y:
						continue
					attackdata.add((Vector2(self.pos.x, y), skill.damage))
				# print(f"attackdata = {attackdata}")
				
			elif skill.attacktype == AttackType.AREA.value:
				# 以角色位置為參考點，角色周圍 n 單位皆受傷害 X
				for x in range(self.pos.x - skill.level, self.pos.x + skill.level + 1):
					if x < -MAX_X or x > MAX_X:
						continue
					for y in range(self.pos.y - skill.level, self.pos.y + skill.level + 1):
						if y < -MAX_Y or y > MAX_Y:
							continue
						attackdata.add((Vector2(x, y), skill.damage))
		for attack in attackdata:
			for entity in entities:
				if entity.pos == attack[0]:
					entity.hp -= attack[1]
					skill.hit_enemy(entity.pos, pygame.time.get_ticks(),1)
				else:
					pass
					skill.hit_enemy(attack[0], pygame.time.get_ticks(),0)
				if entity.hp <= 0:
					self.killed += 1
					self.money += entity.value
				