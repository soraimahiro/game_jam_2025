import pygame
import random
import os
from vector2 import Vector2
from player import Player
from entity import Entity


class Canvas:
	S_TITLE = 0;	S_SETTING = 1;	S_CREDITS = 2
	S_BATTLE = 3;	S_BOSS = 4;		S_SHOP = 5;		S_END = 6
	T_START = 0;	T_SETTING = 1;	T_CREDIT = 2;	T_EXIT = 3
	def __init__(self):
		self.stage = Canvas.S_TITLE
		self.entities = [Entity.random_enemy() for i in range(3)]
		self.player = Player()
		self.shadows = [Entity.shadow(Vector2(0, i)) for i in range(-3, 4)]
		self.round_pass = 0
		self.enemy_wait = 8
		self.new_enemy_count = 2
		self.boss_wait = 20
		pass
	def set_stage(self, stage: int):
		self.previous_stage = self.stage
		self.stage = stage
		print(f"stage set from {self.previous_stage} to {self.stage}")
		self.play_background_music()
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
	def draw_bar(self, screen: pygame.Surface):
		heart = pygame.transform.scale(pygame.image.load("./resource/image/redstone.png"), (50, 50))
		for i in range(self.player.hp):
			screen.blit(heart, (heart.get_width() * 1.1 * i, 0))
		gold = pygame.transform.scale(pygame.image.load("./resource/image/gold_ingot.png"), (50, 50))
		screen.blit(gold, (screen.get_width() - gold.get_width(), 0))
		font = pygame.font.SysFont("NOTOSANSTC-VARIABLEFONT_WGHT.TTF", 48)
		text = font.render(f"{self.player.money} ", 0, (0, 0, 0))
		screen.blit(text, (screen.get_width() - gold.get_width() - text.get_width(), gold.get_height() / 2 - text.get_height() / 3))
		pass
	def draw_title(self, screen: pygame.Surface):
		screen.fill((255, 255, 255))
		font = pygame.font.SysFont("NOTOSANSTC-VARIABLEFONT_WGHT.TTF", 128)
		text = font.render("Our Game", 0, (0, 0, 255), None)
		screen.blit(text, (screen.get_width() * 0.15, screen.get_height() * 0.25))
		font = pygame.font.SysFont("NOTOSANSTC-VARIABLEFONT_WGHT.TTF", 72)
		text = font.render("Start", 0, (0, 0, 0) if self.player.pos.y != Canvas.T_START else (255, 127, 0), None)
		screen.blit(text, (screen.get_width() * 0.15, screen.get_height() * 0.5))
		text = font.render("Setting", 0, (0, 0, 0) if self.player.pos.y != Canvas.T_SETTING else (255, 127, 0), None)
		screen.blit(text, (screen.get_width() * 0.15, screen.get_height() * 0.6))
		text = font.render("Credit", 0, (0, 0, 0) if self.player.pos.y != Canvas.T_CREDIT else (255, 127, 0), None)
		screen.blit(text, (screen.get_width() * 0.15, screen.get_height() * 0.7))
		text = font.render("Exit", 0, (0, 0, 0) if self.player.pos.y != Canvas.T_EXIT else (255, 127, 0), None)
		screen.blit(text, (screen.get_width() * 0.15, screen.get_height() * 0.8))
		pass
	def draw_setting(self, screen: pygame.Surface):
		screen.fill((127, 255, 0))
		font = pygame.font.SysFont("NOTOSANSTC-VARIABLEFONT_WGHT.TTF", 72)
		text = font.render("Here is nothing you can set.", 0, (0, 0, 0), None)
		screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() * 0.5))
		text = font.render("Press Enter to return", 0, (0, 0, 0), None)
		screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() * 0.6))
		pass
	def draw_credit(self, screen: pygame.Surface):
		screen.fill((180, 180, 0))
		font = pygame.font.SysFont("NOTOSANSTC-VARIABLEFONT_WGHT.TTF", 48)
		text = font.render("Credit", 0, (0, 0, 0), None)
		screen.blit(text, (screen.get_width() * 0.15, screen.get_height() * 0.15))
		text = font.render("Press Enter to return", 0, (0, 0, 0), None)
		screen.blit(text, (screen.get_width() * 0.95 - text.get_width(), screen.get_height() * 0.9))
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
		# Draw upper bar
		self.draw_bar(screen)
		pass
	def draw_boss(self, screen: pygame.Surface):
		# fill background
		screen.fill((255, 0, 0))
		# Draw player
		self.draw_unit(screen, self.player)
		# Draw entities
		for entity in self.entities:
			self.draw_unit(screen, entity)
		# Draw upper bar
		self.draw_bar(screen)
		pass
	def draw_win(self, screen: pygame.Surface):
		screen.fill((127, 127, 0))
		font = pygame.font.SysFont("NOTOSANSTC-VARIABLEFONT_WGHT.TTF", 128)
		text = font.render("You Win!!", 0, (0, 0, 0), None)
		screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() * 0.15))
		font = pygame.font.SysFont("NOTOSANSTC-VARIABLEFONT_WGHT.TTF", 48)
		text = font.render("Press Enter to return", 0, (0, 0, 0), None)
		screen.blit(text, (screen.get_width() * 0.95 - text.get_width(), screen.get_height() * 0.9))
		pass
	def draw_lose(self, screen: pygame.Surface):
		screen.fill((72, 72, 72))
		font = pygame.font.SysFont("NOTOSANSTC-VARIABLEFONT_WGHT.TTF", 128)
		text = font.render("You Lose...", 0, (0, 0, 0), None)
		screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() * 0.15))
		font = pygame.font.SysFont("NOTOSANSTC-VARIABLEFONT_WGHT.TTF", 48)
		text = font.render("Press Enter to return", 0, (0, 0, 0), None)
		screen.blit(text, (screen.get_width() * 0.95 - text.get_width(), screen.get_height() * 0.9))
		pass
	def draw(self, screen: pygame.Surface):
		if self.stage == Canvas.S_TITLE:
			self.draw_title(screen)
		elif self.stage == Canvas.S_SETTING:
			self.draw_setting(screen)
		elif self.stage == Canvas.S_CREDITS:
			self.draw_credit(screen)
		elif self.stage == Canvas.S_BATTLE:
			self.draw_battle(screen)
		elif self.stage == Canvas.S_BOSS:
			self.draw_boss(screen)
		elif self.stage == Canvas.S_END:
			if (self.player.hp > 0):
				self.draw_win(screen)
			else:
				self.draw_lose(screen)
		pass
	def pressed_title(self, key) -> bool:
		if key in {pygame.K_w, pygame.K_UP, pygame.K_a, pygame.K_LEFT}:
			self.player.pos.y -= 1
		elif key in {pygame.K_d, pygame.K_DOWN, pygame.K_d, pygame.K_RIGHT}:
			self.player.pos.y += 1
		elif key == pygame.K_RETURN:
			if self.player.pos.y == Canvas.T_START:
				self.set_stage(Canvas.S_BATTLE)
			elif self.player.pos.y == Canvas.T_SETTING:
				self.set_stage(Canvas.S_SETTING)
			elif self.player.pos.y == Canvas.T_CREDIT:
				self.set_stage(Canvas.S_CREDITS)
			elif self.player.pos.y == Canvas.T_EXIT:
				return False
		self.player.pos.y %= 4
		return True
	def pressed_setting(self, key) -> bool:
		if key == pygame.K_RETURN:
			self.set_stage(self.previous_stage)
		return True
	def pressed_credit(self, key) -> bool:
		if key == pygame.K_RETURN:
			self.set_stage(self.previous_stage)
		return True
	def pressed_battle(self, key) -> bool:
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
				for entity in self.entities:
					if entity.pos == self.player.pos and entity.move.x > 0:
						self.player.hp -= entity.damage
						print(f"hp = {self.player.hp}")
				for shadow in self.shadows:
					if shadow.pos.y == self.player.pos.y:
						shadow.pos.x = self.player.pos.x
				self.next_round()
		elif key in {pygame.K_d, pygame.K_RIGHT}:
			if (self.player.pos.x < 5):
				self.player.pos.x += 1
				for entity in self.entities:
					if entity.pos == self.player.pos and entity.move.x < 0:
						self.player.hp -= entity.damage
						print(f"hp = {self.player.hp}")
				for shadow in self.shadows:
					if shadow.pos.y == self.player.pos.y:
						shadow.pos.x = self.player.pos.x
				self.next_round()
		return True
	def pressed_boss(self, key) -> bool:
		if key in {pygame.K_w, pygame.K_UP}:
			if self.player.pos.y > -3:
				self.player.pos.y -= 1
				for entity in self.entities:
					if entity.pos == self.player.pos and entity.move.y < 0 and entity.move.x == 0:
						self.player.hp -= entity.damage
						print(f"hp = {self.player.hp}")
				self.next_round()
		elif key in {pygame.K_s, pygame.K_DOWN}:
			if self.player.pos.y < 3:
				self.player.pos.y += 1
				for entity in self.entities:
					if entity.pos == self.player.pos and entity.move.y > 0 and entity.move.x == 0:
						self.player.hp -= entity.damage
						print(f"hp = {self.player.hp}")
				self.next_round()
		elif key in {pygame.K_a, pygame.K_LEFT}:
			if (self.player.pos.x > -5):
				self.player.pos.x -= 1
				for entity in self.entities:
					if entity.pos == self.player.pos and entity.move.x > 0 and entity.move.y == 0:
						self.player.hp -= entity.damage
						print(f"hp = {self.player.hp}")
				self.next_round()
		elif key in {pygame.K_d, pygame.K_RIGHT}:
			if (self.player.pos.x < 5):
				self.player.pos.x += 1
				for entity in self.entities:
					if entity.pos == self.player.pos and entity.move.x < 0 and entity.move.y == 0:
						self.player.hp -= entity.damage
						print(f"hp = {self.player.hp}")
				self.next_round()
		return True
	def pressed_end(self, key) -> bool:
		if key == pygame.K_RETURN:
			self.set_stage(Canvas.S_TITLE)
		return True
	def pressed(self, key: int) -> bool:
		if self.stage == Canvas.S_TITLE:
			return self.pressed_title(key)
		elif self.stage == Canvas.S_SETTING:
			return self.pressed_setting(key)
		elif self.stage == Canvas.S_CREDITS:
			return self.pressed_credit(key)
		elif self.stage == Canvas.S_BATTLE:
			return self.pressed_battle(key)
		elif self.stage == Canvas.S_BOSS:
			return self.pressed_boss(key)
		elif self.stage == Canvas.S_END:
			return self.pressed_end(key)
		return False
	def next_round(self):
		for entity in self.entities:
			entity.next_step(self.player)
			# check when boss move 
			if entity.pos == self.player.pos:
				self.player.hp -= entity.damage
				print(f"hp = {self.player.hp}")
			self.player.attack(entity)
		if not self.player.hp > 0:
			self.set_stage(Canvas.S_END)
		for entity in self.entities:
			if entity.hp <= 0:
				if entity.type == Entity.T_BOSS:
					self.stage = Canvas.S_END
				self.entities.remove(entity)
		self.round_pass += 1
		if self.round_pass == self.boss_wait:
			self.stage = Canvas.S_BOSS
			self.entities.append(Entity.random_boss())
			self.enemy_wait *= 2
		elif self.round_pass % self.enemy_wait == 0:
			for i in range(self.new_enemy_count):
				self.entities.append(Entity.random_enemy())
		pass
	def play_background_music(self):
		bgm_path = "./resource/bgm/"
		if self.stage == Canvas.S_TITLE:
			bgm_file = "bgm_menu_DustyRoadMagic.mp3"
		elif self.stage == Canvas.S_SETTING:
			bgm_file = "bgm_menu_LastCappuccinoInRio.mp3"
		elif self.stage == Canvas.S_BATTLE:
			bgm_file = "bgm_mob_Matterhorn.mp3"
		elif self.stage == Canvas.S_BOSS:
			bgm_file = "bgm_boss_Future.mp3"
		elif self.stage == Canvas.S_END:
			bgm_file = "bgm_menu_TreasureHunt.mp3"
		elif self.stage == Canvas.S_CREDITS:
			# todo: add credits music
			bgm_file = "bgm_menu_DustyRoadMagic.mp3"
			pass
		elif self.stage == Canvas.S_SHOP:
			bgm_file = "bgm_shop_SunriseFromAMoonbeam.mp3"
		else:
			return
		pygame.mixer.music.load(os.path.join(bgm_path, bgm_file))
		pygame.mixer.music.play(-1)