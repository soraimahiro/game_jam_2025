import pygame
from vector2 import Vector2
from player import Player
from entity import Entity

class Canvas:
	def __init__(self):
		self.entities = [Entity() for i in range(3)]
		self.player = Player()
	def draw_unit(self, screen: pygame.Surface, entity: Player | Entity):
		width = screen.get_width()
		height = screen.get_height()
		center = Vector2(width, height) / 2
		delta = min((height - 50) / 6, width / 10)
		shift = Vector2(entity.icon.get_width(), entity.icon.get_height()) / 2
		position = center + entity.pos * delta - shift
		screen.blit(entity.icon, position.to_tuple())
		pass
	def draw(self, screen: pygame.Surface):
		# fill background
		screen.fill((127, 127, 255))
		# Draw player
		self.draw_unit(screen, self.player)
		# Draw entities
		for entity in self.entities:
			self.draw_unit(screen, entity)
