import pygame
from vector2 import Vector2

class Skill:
	def __init__(self, damage : int, range : int, direction : int):
		self.damage = damage
		self.range = range
		self.direction = direction # 我不太懂這個是做什麼的，不同數字表示不同攻擊模式?
		pass