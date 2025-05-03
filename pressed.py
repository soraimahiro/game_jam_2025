import pygame
from stage import Stage, StageOption, TitleOption, SettingOption
from music import change_music_volume
import globals
def pressed_title(stage: Stage, key) -> bool:
	if key in {pygame.K_w, pygame.K_UP, pygame.K_a, pygame.K_LEFT}:
		stage.player.pos.y -= 1
	elif key in {pygame.K_s, pygame.K_DOWN, pygame.K_d, pygame.K_RIGHT}:
		stage.player.pos.y += 1
	elif key == pygame.K_RETURN:
		if stage.player.pos.y == TitleOption.START.value:
			stage.set_stage(StageOption.BATTLE)
		elif stage.player.pos.y == TitleOption.SETTING.value:
			stage.set_stage(StageOption.SETTING)
		elif stage.player.pos.y == TitleOption.CREDIT.value:
			stage.set_stage(StageOption.CREDITS)
		elif stage.player.pos.y == TitleOption.EXIT.value:
			return False
	stage.player.pos.y %= 4
	return True

def pressed_setting(stage: Stage, key) -> bool:
	print(f"x,y = {stage.player.pos.x,stage.player.pos.y}")
	if stage.player.pos.x == 0:
		if key in {pygame.K_w, pygame.K_UP}:
			stage.player.pos.y -= 1
		elif key in {pygame.K_s, pygame.K_DOWN}:
			stage.player.pos.y += 1
		elif key in {pygame.K_RETURN}:
			if stage.player.pos.y == SettingOption.SKIN.value:
				stage.player.pos.x = 1
			elif stage.player.pos.y == SettingOption.SOUND.value:
				stage.player.pos.x = 1
			elif stage.player.pos.y == SettingOption.EXIT.value:
				stage.player.pos.x = 0
				stage.player.pos.y = 1
				stage.set_stage(StageOption.TITLE)
	elif stage.player.pos.x == 1:
		if stage.player.pos.y == SettingOption.SKIN.value:
			if key in {pygame.K_w, pygame.K_UP}:
				pass
			elif key in {pygame.K_s, pygame.K_DOWN}:
				pass
		elif stage.player.pos.y == SettingOption.SOUND.value:
			if key in {pygame.K_w, pygame.K_UP}:
				globals.music_volume += 1 if globals.music_volume < 100 else 0
			elif key in {pygame.K_s, pygame.K_DOWN}:
				globals.music_volume -= 1 if globals.music_volume > 0 else 0
			elif key in {pygame.K_d, pygame.K_RIGHT}:
				if globals.music_volume < 96:
					globals.music_volume += 5
				else:
					globals.music_volume = 100
			elif key in {pygame.K_a, pygame.K_LEFT}:
				if globals.music_volume > 4:
					globals.music_volume -= 5
				else:
					globals.music_volume = 0
			elif key in {pygame.K_RETURN}:
				stage.player.pos.x = 0
			change_music_volume(globals.music_volume)
	print(f"x,y = {stage.player.pos.x,stage.player.pos.y}, volume = {globals.music_volume}")
	
	if key == pygame.K_ESCAPE:
		stage.player.pos.x = 0
		stage.player.pos.y = 1
		stage.set_stage(StageOption.TITLE)
	
	return True

def pressed_credit(stage: Stage, key) -> bool:
	if key == pygame.K_RETURN:
		stage.set_stage(stage.previous_stage)
	return True

def pressed_battle(stage: Stage, key) -> bool:
	if key == pygame.K_ESCAPE:
		stage.esc_menu.show = True
	elif key in {pygame.K_w, pygame.K_UP}:
		if stage.player.pos.y > -3:
			stage.player.pos.y -= 1
			for shadow in stage.shadows:
				if stage.player.pos.y == shadow.pos.y:
					stage.player.pos.x = shadow.pos.x
			stage.next_round()
	elif key in {pygame.K_s, pygame.K_DOWN}:
		if stage.player.pos.y < 3:
			stage.player.pos.y += 1
			for shadow in stage.shadows:
				if stage.player.pos.y == shadow.pos.y:
					stage.player.pos.x = shadow.pos.x
			stage.next_round()
	elif key in {pygame.K_a, pygame.K_LEFT}:
		if (stage.player.pos.x > -5):
			stage.player.pos.x -= 1
			for entity in stage.entities:
				if entity.pos == stage.player.pos and entity.move.x > 0:
					stage.player.hp -= entity.damage
					print(f"hp = {stage.player.hp}")
			for shadow in stage.shadows:
				if shadow.pos.y == stage.player.pos.y:
					shadow.pos.x = stage.player.pos.x
			stage.next_round()
	elif key in {pygame.K_d, pygame.K_RIGHT}:
		if (stage.player.pos.x < 5):
			stage.player.pos.x += 1
			for entity in stage.entities:
				if entity.pos == stage.player.pos and entity.move.x < 0:
					stage.player.hp -= entity.damage
					print(f"hp = {stage.player.hp}")
			for shadow in stage.shadows:
				if shadow.pos.y == stage.player.pos.y:
					shadow.pos.x = stage.player.pos.x
			stage.next_round()
	return True

def pressed_boss(stage: Stage, key) -> bool:
	if key == pygame.K_ESCAPE:
		stage.esc_menu.show = True
	elif key in {pygame.K_w, pygame.K_UP}:
		if stage.player.pos.y > -3:
			stage.player.pos.y -= 1
			for entity in stage.entities:
				if entity.pos == stage.player.pos and entity.move.y < 0 and entity.move.x == 0:
					stage.player.hp -= entity.damage
					print(f"hp = {stage.player.hp}")
			stage.next_round()
	elif key in {pygame.K_s, pygame.K_DOWN}:
		if stage.player.pos.y < 3:
			stage.player.pos.y += 1
			for entity in stage.entities:
				if entity.pos == stage.player.pos and entity.move.y > 0 and entity.move.x == 0:
					stage.player.hp -= entity.damage
					print(f"hp = {stage.player.hp}")
			stage.next_round()
	elif key in {pygame.K_a, pygame.K_LEFT}:
		if (stage.player.pos.x > -5):
			stage.player.pos.x -= 1
			for entity in stage.entities:
				if entity.pos == stage.player.pos and entity.move.x > 0 and entity.move.y == 0:
					stage.player.hp -= entity.damage
					print(f"hp = {stage.player.hp}")
			stage.next_round()
	elif key in {pygame.K_d, pygame.K_RIGHT}:
		if (stage.player.pos.x < 5):
			stage.player.pos.x += 1
			for entity in stage.entities:
				if entity.pos == stage.player.pos and entity.move.x < 0 and entity.move.y == 0:
					stage.player.hp -= entity.damage
					print(f"hp = {stage.player.hp}")
			stage.next_round()
	return True

def pressed_end(stage: Stage, key) -> bool:
	if key == pygame.K_RETURN:
		stage.reset()
	return True

def pressed_esc_menu(stage: Stage, key):
	if key in {pygame.K_w, pygame.K_UP, pygame.K_a, pygame.K_LEFT}:
		stage.esc_menu.option -= 1
	elif key in {pygame.K_s, pygame.K_DOWN, pygame.K_d, pygame.K_RIGHT}:
		stage.esc_menu.option += 1
	elif key == pygame.K_ESCAPE:
		stage.esc_menu.show = False
	elif key == pygame.K_RETURN:
		if stage.esc_menu.option == 0:
			stage.esc_menu.show = False
		elif stage.esc_menu.option == 1:
			stage.reset()
	stage.esc_menu.option %= 2
	return True

def pressed_story(stage: Stage, key) -> bool:
	if key == pygame.K_RETURN:
		stage.set_stage(StageOption.BATTLE)
	return True

def pressed(stage: Stage, key) -> bool:
	if stage.esc_menu.show:
		return pressed_esc_menu(stage, key)
	elif stage.stage == StageOption.TITLE:
		return pressed_title(stage, key)
	elif stage.stage == StageOption.SETTING:
		return pressed_setting(stage, key)
	elif stage.stage == StageOption.CREDITS:
		return pressed_credit(stage, key)
	elif stage.stage == StageOption.BATTLE_STORY:
		return pressed_story(stage, key)
	elif stage.stage == StageOption.BATTLE:
		return pressed_battle(stage, key)
	elif stage.stage == StageOption.BOSS:
		return pressed_boss(stage, key)
	elif stage.stage == StageOption.END:
		return pressed_end(stage, key)
	return False