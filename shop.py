import random
from entity import Entity
from vector2 import Vector2
from player import Player

class Shop:
	def __init__(self, player: Player):
		self.option = 0
		weight = [10 for i in range(5)]
		for skill in player.skills:
			weight[skill.attacktype] += 10 - skill.level * 2
		self.goods = random.choices(range(5), weight, k = 3)

