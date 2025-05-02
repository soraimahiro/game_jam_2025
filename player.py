import pygame
from vector2 import Vector2
from skill import Skill

# Player(x, y, width, height)
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.pos = Vector2(0, 0)
		self.icon = pygame.transform.scale(pygame.image.load("./resource/image/diamond.png"), (75, 75))
		self.money = 0
		self.hp = 10
		self.skills = [Skill(1, 3, 0)] # 預設為射程3傷害1的十字攻擊
		pass
	def attack(self, entity):
		if entity.hp <= 0:
			return
		for skill in self.skills:
			if skill.direction == 0:
				if entity.pos.y == self.pos.y and entity.pos.x >= self.pos.x - skill.range and entity.pos.x <= self.pos.x + skill.range:
					entity.hp -= skill.damage
					print (f"entity hp = {entity.hp}")
				elif entity.pos.x == self.pos.x and entity.pos.y >= self.pos.y - skill.range and entity.pos.y <= self.pos.y + skill.range:
					entity.hp -= skill.damage
					print (f"entity hp = {entity.hp}")
		if entity.hp <= 0:
			self.money += 1 # 這個感覺可以換成+=entity.value，但目前沒有這個設定
			print (f"money = {self.money}")