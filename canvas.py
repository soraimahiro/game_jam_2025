import pygame
import random
from vector2 import Vector2
from player import Player
from entity import Entity

class Canvas:
	S_TITLE = 0;	S_SETTING = 1;	S_CREDITS = 2
	S_BATTLE = 3;	S_BOSS = 4;		S_SHOP = 5;		S_END = 6
	def __init__(self):
		self.stage = Canvas.S_BATTLE
		self.entities = [Entity(
			"./resource/image/iron_ingot.png",
			Entity.T_MOSTER,
			1,
			Vector2(j * -5, random.randrange(-3, 3)),
			Vector2(j, 0)
		) for j in [random.choice((-1, 1))] for i in range(3)]
		self.player = Player()
		self.shadows = [Entity(
			"./resource/image/emerald.png",
			Entity.T_SHADOW,
			-1,
			Vector2(0, i),
			Vector2(0, 0)
		) for i in range(-3, 4)]
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
		# Draw shadows
		for shadow in self.shadows:
			if not shadow.pos.y == self.player.pos.y:
				self.draw_unit(screen, shadow)
		# Draw entities
		for entity in self.entities:
			self.draw_unit(screen, entity)
		pass
	def pressed_battle(self, key):
		if key in {pygame.K_w, pygame.K_UP}:
			if self.player.pos.y > -3:
				self.player.pos.y -= 1
				for shadow in self.shadows:
					if self.player.pos.y == shadow.pos.y:
						self.player.pos.x = shadow.pos.x
				self.next_round()
		elif key in {pygame.K_s, pygame.K_DOWN}:
			if self.player.pos.y < 3:
				self.player.pos.y += 1
				for shadow in self.shadows:
					if self.player.pos.y == shadow.pos.y:
						self.player.pos.x = shadow.pos.x
				self.next_round()
		elif key in {pygame.K_a, pygame.K_LEFT}:
			if (self.player.pos.x > -5):
				self.player.pos.x -= 1
				for shadow in self.shadows:
					if shadow.pos.y == self.player.pos.y:
						shadow.pos.x = self.player.pos.x
				self.next_round()
		elif key in {pygame.K_d, pygame.K_RIGHT}:
			if (self.player.pos.x < 5):
				self.player.pos.x += 1
				for shadow in self.shadows:
					if shadow.pos.y == self.player.pos.y:
						shadow.pos.x = self.player.pos.x
				self.next_round()
	def pressed_boss(self, key):
		if key in {pygame.K_w, pygame.K_UP}:
			if self.player.pos.y > -3:
				self.player.pos.y -= 1
				self.next_round()
		elif key in {pygame.K_s, pygame.K_DOWN}:
			if self.player.pos.y < 3:
				self.player.pos.y += 1
				self.next_round()
		elif key in {pygame.K_a, pygame.K_LEFT}:
			if (self.player.pos.x > -5):
				self.player.pos.x -= 1
				self.next_round()
		elif key in {pygame.K_d, pygame.K_RIGHT}:
			if (self.player.pos.x < 5):
				self.player.pos.x += 1
				self.next_round()
	def draw(self, screen: pygame.Surface):
		if (self.stage == Canvas.S_BATTLE):
			self.draw_battle(screen)
		elif (self.stage == Canvas.S_BOSS):
			self.draw_boss(screen)
	def pressed(self, key: int):
		if (self.stage == Canvas.S_BATTLE):
			self.pressed_battle(key)
		elif (self.stage == Canvas.S_BOSS):
			self.pressed_boss(key)
	def next_round(self):
		for entity in self.entities:
			entity.next_step()
		pass