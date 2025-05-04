import pygame
from vector2 import Vector2
from skill import Skill
import globals
from skill import AttackType
import random
import os
from typing import TYPE_CHECKING
from music import play_sound_effect
if TYPE_CHECKING:
	from entity import Entity
# Player(x, y, width, height)

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.pos = Vector2(0, 0)
		self.pre_pos = Vector2(0, 0)
		self.money = 100
		self.hp = 10
		self.killed = 0
		self.skills = [Skill(1, 1, AttackType.LINE_XY)] # 預設為射程3傷害1的十字攻擊
		pass

	def icon(self):
		return globals.icon(f"./resource/image/{globals.get_player_img()}.png")
	
	def move(self, move: Vector2):
		self.pre_pos = Vector2(self.pos.x, self.pos.y)
		self.pos += move
		pass
	
	def attack(self, entities: list['Entity']):
		# for entity in entities:
		attackdata: set[tuple[Vector2, int]] = set()
		MAX_X=5
		MAX_Y=3
		KILLED = False
		# if entity.hp <= 0:
		# 	return
		for skill in self.skills:
			if skill.attacktype == AttackType.POINT:
				# 隨機 n 個位置
				for i in range(skill.level):
					x = random.randint(-MAX_X, MAX_X)
					y = random.randint(-MAX_Y, MAX_Y)
					attackdata.add((Vector2(x, y), skill.damage))
			elif skill.attacktype == AttackType.LINE_X:
				# x方向；以角色位置為參考點，x方向距離 n 單位內的敵人受傷害 X
				for x in range(self.pos.x - skill.level, self.pos.x + skill.level + 1):
					if x < -MAX_X or x > MAX_X:
						continue
					attackdata.add((Vector2(x, self.pos.y), skill.damage))
			elif skill.attacktype == AttackType.LINE_Y:
				# y方向；以角色位置為參考點，y方向距離 n 單位內的敵人受傷害 X
				for y in range(self.pos.y - skill.level, self.pos.y + skill.level + 1):
					if y < -MAX_Y or y > MAX_Y:
						continue
					attackdata.add((Vector2(self.pos.x, y), skill.damage))
			elif skill.attacktype == AttackType.LINE_XY:
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
			elif skill.attacktype == AttackType.AREA:
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
				if entity.hp <= 0:
					continue
				if entity.pos == attack[0]:
					entity.hp -= attack[1]
					skill.hit_enemy(entity.pos, pygame.time.get_ticks(), 1)
				else:
					skill.hit_enemy(attack[0], pygame.time.get_ticks(),0)
				if entity.hp <= 0:
					self.killed += 1
					KILLED = True
					self.money += entity.value
		if KILLED:
			play_sound_effect("enemy_dead")
		else:
			play_sound_effect("move")