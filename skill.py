import pygame
from vector2 import Vector2
from entity import Entity

class Skill:
	def __init__(self, damage : int, range : int, direction : int):
		self.damage = damage
		self.range = range
		self.direction = direction # 我不太懂這個是做什麼的，不同數字表示不同攻擊模式?
		self.hits = []
		pass
	def hit_enemy(self, pos : Vector2, start_time : int):
		self.hits.append(Hit.hit(pos, start_time))
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
	def hit(self, pos : Vector2, start_time : int):
		entity = Entity("./resource/image/type_simple/image_hit.png", Entity.T_HIT, 1, 0, pos, {0, 0})
		return Hit(entity, Hit.HIT_DURATION, start_time)