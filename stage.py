from vector2 import Vector2
from player import Player
from entity import Entity
from shop import Shop
from music import play_background_music
from music import change_music_volume
from enum import Enum, auto
from setting import Esc_menu
import random

import globals

class StageOption(Enum):
	TITLE = auto()
	SETTING = auto()
	CREDITS = auto()
	BATTLE_STORY = auto()
	BATTLE = auto()
	BOSS = auto()
	SHOP = auto()
	END = auto()

class TitleOption(Enum):
	START = 0
	SETTING = 1
	CREDIT = 2
	EXIT = 3

class SettingOption(Enum):
	SKIN = 0
	SOUND = 1
	EXIT = 2


class Stage:
	def __init__(self):
		self.reset()
		pass
	
	def set_stage(self, stage: StageOption):
		self.previous_stage = self.stage
		self.stage = stage
		if stage == StageOption.SHOP:
			self.shop_info = Shop(self.player)
		elif stage == StageOption.END:
			globals.enemy_killed += self.player.killed
			globals.step_moved += self.round_pass
		if stage == StageOption.SETTING:
			self.player.pos.x = 0
			self.player.pos.y = 0
		print(f"stage set from {self.previous_stage} to {self.stage}")
		play_background_music(self)
		change_music_volume(globals.music_volume)
		# change_sound_effect_volume(self.volume)
		pass
	
	def next_round(self):
		go_shop = False
		for entity in self.entities:
			pre_pos = Vector2(entity.pos.x, entity.pos.y)
			entity.next_step(self.player)
			# check when boss move 
			if Vector2.intercept(self.player.pre_pos, self.player.pos, pre_pos, entity.pos):
				self.player.hp -= entity.damage
				if entity.type == Entity.T_SHOP:
					go_shop = True
					entity.hp = 0
				elif entity.type == Entity.T_REGEN:
					entity.hp = 0
				#print(f"hp = {self.player.hp}")
		self.player.attack(self.entities)
		if go_shop:
			self.set_stage(StageOption.SHOP)
		if not self.player.hp > 0:
			self.set_stage(StageOption.END)
		for entity in self.entities:
			if entity.type == Entity.T_SHOP:
				entity.hp -= 5
			if entity.hp <= 0:
				if entity.type == Entity.T_BOSS:
					self.set_stage(StageOption.END)
				self.entities.remove(entity)
		self.round_pass += 1
		if self.stage != StageOption.END and self.round_pass >= self.boss_wait:
			if not Entity.T_BOSS in [enemy.type for enemy in self.entities]:
				self.set_stage(StageOption.BOSS)
				self.entities.append(Entity.random_boss())
				self.enemy_wait = self.enemy_wait * 3 // 2
		if self.round_pass % self.enemy_wait == 0:
			for i in range(self.new_enemy_count):
				self.entities.append(Entity.random_enemy(self.stage == StageOption.BOSS, 1))
		if self.round_pass % self.recover_wait == 0:
			if random.choice((True, False)):
				randpos = Vector2(
					random.choice([x for x in range(-5, 6) if abs(x - self.player.pos.x) > 2]),
					random.choice([y for y in range(-3, 4) if abs(y - self.player.pos.y) > 2]))
				self.entities.append(Entity("shop/image_blood_add_1", Entity.T_REGEN, 100, -1, randpos, Vector2(0, 0), 0, 1, 0))
		if self.player.money >= 10 and self.player.killed > 5 and not Entity.T_SHOP in [e.type for e in self.entities]:
			if random.randint(0, 9) < 2:
				randpos = Vector2(
					random.choice([x for x in range(-5, 6) if abs(x - self.player.pos.x) > 2]),
					random.choice([y for y in range(-3, 4) if abs(y - self.player.pos.y) > 2]))
				self.entities.append(Entity("type_simple/image_shop", Entity.T_SHOP, 100, 0, randpos, Vector2(0, 0), 0, 1, 0))
		pass
	
	def reset(self):
		self.stage = StageOption.TITLE
		self.previous_stage = self.stage
		self.entities = [Entity.random_enemy(False) for i in range(3)]
		self.player = Player()
		self.shadows = [Entity.shadow(Vector2(0, i)) for i in range(-3, 4)]
		self.round_pass = 0
		self.enemy_wait = 4
		self.new_enemy_count = 2
		self.recover_wait = 6
		self.boss_wait = 50
		self.esc_menu = Esc_menu()
		self.shop_info = Shop(self.player)
		play_background_music(self)