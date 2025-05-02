import pygame
from vector2 import Vector2
from player import Player
from entity import Entity

class Canvas:
	def __init__(self, screen: pygame.Surface):
		self.entities = []
		self.player = Player()
		self.width = screen.get_width()
		self.height = screen.get_height()
	def canvas_pos(self, entity: Player | Entity):
		center = Vector2(self.width, self.height) / 2
		delta = min((self.height - 50) / 6, self.width / 10)
		shift = Vector2(entity.icon.get_width(), entity.icon.get_height()) / 2
		return center + entity.pos * delta - shift
	def draw(self, screen: pygame.Surface):
		self.width = screen.get_width()
		self.height = screen.get_height()
		screen.fill((127, 127, 255)) # background
		# Draw player
		screen.blit(self.player.icon, self.canvas_pos(self.player).to_tuple())

