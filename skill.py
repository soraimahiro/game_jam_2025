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
	def __init__(self, damage : int, level : int, attacktype : int):
		self.damage = damage
		self.level = level
		self.attacktype = attacktype
		self.hits = []
		pass
	def __str__(self):
		return f"Skill(damage={self.damage}, level={self.level}, direction={self.attacktype})"
	def hit_enemy(self, pos : Vector2, start_time : int, is_hit : int):
		self.hits.append(Hit.hit(pos, start_time, is_hit))
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
	def hit(self, pos : Vector2, start_time : int, is_hit : int):
		entity = Entity("type_simple/image_hit", Entity.T_HIT, 1, 0, pos, {0, 0})
		if is_hit == 1:
			#透明度設為255
			entity.icon(255)
			pass
		else:
			#透明度設為10
			entity.icon(10)
			pass
		return Hit(entity, Hit.HIT_DURATION, start_time)