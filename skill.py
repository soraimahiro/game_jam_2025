import pygame
from vector2 import Vector2
from entity import Entity
from enum import Enum

class AttackType(Enum):
    POINT = 0      # 點攻擊：隨機 n 個位置傷害 X
    LINE_X = 1     # 線攻擊：x方向；以角色位置為參考點，x方向距離 n 單位內的敵人受傷害 X
    LINE_Y = 2     # 線攻擊：y方向；以角色位置為參考點，y方向距離 n 單位內的敵人受傷害 X
    LINE_XY = 3    # 線攻擊：xy方向；以角色位置為參考點，xy方向距離 n 單位內的敵人受傷害 X
    AREA = 4       # 面攻擊：以角色位置為參考點，角色周圍 n 單位皆受傷害 X

class Skill:
	def __init__(self, damage : int, level : int, attacktype : AttackType):
		self.damage = damage
		self.level = level
		self.attacktype = attacktype
		self.hits = []
		pass
	def __str__(self):
		return f"Skill(damage={self.damage}, level={self.level}, direction={self.attacktype})"
	def cost(self):
		if self.attacktype == AttackType.AREA:
			if self.level in {0, 1, 2}:
				return 15 + 5 * self.level
			return 50
		if self.attacktype in {AttackType.LINE_X, AttackType.LINE_Y}:
			if self.level in {0, 1, 2}:
				return 5 + 3 * self.level
			return 15
		if self.attacktype == AttackType.LINE_XY:
			if self.level in {0, 1, 2}:
				return 7 + 4 * self.level
			return 20
		if self.attacktype == AttackType.POINT:
			return 3 + 3 * self.level
		return 65535
	def hit_enemy(self, pos : Vector2, start_time : int, is_hit : int, attacktype : AttackType):
		self.hits.append(Hit.hit(pos, start_time, is_hit, attacktype))
	def update(self, current_time : int):
		for hit in self.hits:
			if (current_time - hit.start_time >= hit.duration):
				self.hits.remove(hit)
	
class Hit:
	HIT_DURATION = 100
	def __init__(self, entity : Entity, duration : int, start_time : int):
		self.entity = entity
		self.duration = duration
		self.start_time = start_time

	@ classmethod
	def hit(self, pos : Vector2, start_time : int, is_hit : int, attacktype : AttackType):
		file_path = "type_simple/image_hit"
		if attacktype == AttackType.POINT:
			file_path = "type_simple/image_hit_dot"
		elif attacktype == AttackType.LINE_X:
			file_path = "type_simple/image_hit_line"
		elif attacktype == AttackType.LINE_Y:
			file_path = "type_simple/image_hit_line"
		elif attacktype == AttackType.LINE_XY:
			file_path = "type_simple/image_hit_line"
		elif attacktype == AttackType.AREA:
			file_path = "type_simple/image_hit_area"
		
		entity = Entity(file_path, Entity.T_HIT, 1, 0, pos, Vector2(0, 0))
		if is_hit == 1:
			#透明度設為255
			entity.img_alpha = 255
			pass
		else:
			#透明度設為10
			entity.img_alpha = 10
			pass
		return Hit(entity, Hit.HIT_DURATION, start_time)
	