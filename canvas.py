import pygame
from vector2 import Vector2
from player import Player
from entity import Entity

class Canvas:
	S_TITLE = 0;	S_SETTING = 1;	S_CREDITS = 2
	S_BATTLE = 3;	S_SHOP = 4;		S_END = 5
	def __init__(self):
		self.stage = Canvas.S_BATTLE
		self.entities = [Entity() for i in range(3)]
		self.player = Player()
		pass
	def draw_unit(self, screen: pygame.Surface, entity: Player | Entity):
		width = screen.get_width()
		height = screen.get_height()
		center = Vector2(width, height) / 2
		# 共 7 條橫線和 11 條 直線，各分 8 塊和 12 塊
		delta = min((height - 50) / 8, width / 12)
		shift = Vector2(entity.icon.get_width(), entity.icon.get_height()) / 2
		position = center + entity.pos * delta - shift
		screen.blit(entity.icon, position.to_tuple())
		pass
	def draw_battle(self, screen: pygame.Surface):
		# fill background
		screen.fill((255, 127, 127))
		# Draw player
		self.draw_unit(screen, self.player)
		# Draw entities
		for entity in self.entities:
			self.draw_unit(screen, entity)
		pass
	def draw(self, screen: pygame.Surface):
		if (self.stage == Canvas.S_BATTLE):
			self.draw_battle(screen)
	def next_round(self):
		pass