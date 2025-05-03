import pygame
from vector2 import Vector2
from stage import Stage, StageOption, TitleOption

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
	if key == pygame.K_RETURN:
		stage.set_stage(stage.previous_stage)
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
			stage.player.move(Vector2(0, -1))
			for shadow in stage.shadows:
				if stage.player.pos.y == shadow.pos.y:
					stage.player.pos.x = shadow.pos.x
					stage.player.pre_pos = stage.player.pos
			stage.next_round()
	elif key in {pygame.K_s, pygame.K_DOWN}:
		if stage.player.pos.y < 3:
			stage.player.move(Vector2(0, 1))
			for shadow in stage.shadows:
				if stage.player.pos.y == shadow.pos.y:
					stage.player.pos.x = shadow.pos.x
					stage.player.pre_pos = stage.player.pos
			stage.next_round()
	elif key in {pygame.K_a, pygame.K_LEFT}:
		if stage.player.pos.x > -5:
			stage.player.move(Vector2(-1, 0))
			for shadow in stage.shadows:
				if shadow.pos.y == stage.player.pos.y:
					shadow.pos.x = stage.player.pos.x
			stage.next_round()
	elif key in {pygame.K_d, pygame.K_RIGHT}:
		if stage.player.pos.x < 5:
			stage.player.move(Vector2(1, 0))
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
			stage.player.move(Vector2(0, -1))
			stage.next_round()
	elif key in {pygame.K_s, pygame.K_DOWN}:
		if stage.player.pos.y < 3:
			stage.player.move(Vector2(0, 1))
			stage.next_round()
	elif key in {pygame.K_a, pygame.K_LEFT}:
		if stage.player.pos.x > -5:
			stage.player.move(Vector2(-1, 0))
			stage.next_round()
	elif key in {pygame.K_d, pygame.K_RIGHT}:
		if stage.player.pos.x < 5:
			stage.player.move(Vector2(1, 0))
			stage.next_round()
	return True

def pressed_end(stage: Stage, key) -> bool:
	if key == pygame.K_RETURN:
		stage.reset()
	return True

def pressed_esc_menu(stage: Stage, key: int):
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

def pressed(stage: Stage, key) -> bool:
	if stage.esc_menu.show:
		return pressed_esc_menu(stage, key)
	elif stage.stage == StageOption.TITLE:
		return pressed_title(stage, key)
	elif stage.stage == StageOption.SETTING:
		return pressed_setting(stage, key)
	elif stage.stage == StageOption.CREDITS:
		return pressed_credit(stage, key)
	elif stage.stage == StageOption.BATTLE:
		return pressed_battle(stage, key)
	elif stage.stage == StageOption.BOSS:
		return pressed_boss(stage, key)
	elif stage.stage == StageOption.END:
		return pressed_end(stage, key)
	return False