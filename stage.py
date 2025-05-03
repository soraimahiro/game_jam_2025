from vector2 import Vector2
from player import Player
from entity import Entity
from our_statistics import Statistics
from music import play_background_music
from enum import Enum

class StageOption(Enum):
	TITLE = 0
	SETTING = 1
	CREDITS = 2
	BATTLE = 3
	BOSS = 4
	SHOP = 5
	END = 6

class TitleOption(Enum):
	START = 0
	SETTING = 1
	CREDIT = 2
	EXIT = 3

class Stage:
	def __init__(self):
		self.reset()
		pass	
	
	def set_stage(self, stage: StageOption):
		self.previous_stage = self.stage
		self.stage = stage
		if stage == StageOption.END:
			Statistics.enemy_killed += self.player.killed
			Statistics.step_moved += self.round_pass
		print(f"stage set from {self.previous_stage} to {self.stage}")
		play_background_music(self)
		pass		
	
	def next_round(self):
		for entity in self.entities:
			entity.next_step(self.player)
			# check when boss move 
			if entity.pos == self.player.pos:
				self.player.hp -= entity.damage
				print(f"hp = {self.player.hp}")
			self.player.attack(entity)
		if not self.player.hp > 0:
			self.set_stage(StageOption.END)
		for entity in self.entities:
			if entity.hp <= 0:
				if entity.type == Entity.T_BOSS:
					self.set_stage(StageOption.END)
				self.entities.remove(entity)
		self.round_pass += 1
		if self.stage != StageOption.END and self.round_pass >= self.boss_wait - self.player.killed:
			if not Entity.T_BOSS in [enemy.type for enemy in self.entities]:
				self.set_stage(StageOption.BOSS)
				self.entities.append(Entity.random_boss())
				self.enemy_wait *= 2
		elif self.round_pass % self.enemy_wait == 0:
			for i in range(self.new_enemy_count):
				self.entities.append(Entity.random_enemy())
	
	def reset(self):
		self.stage = StageOption.TITLE
		self.entities = [Entity.random_enemy() for i in range(3)]
		self.player = Player()
		self.shadows = [Entity.shadow(Vector2(0, i)) for i in range(-3, 4)]
		self.round_pass = 0
		self.enemy_wait = 8
		self.new_enemy_count = 2
		self.boss_wait = 50
		self.statistics = Statistics()