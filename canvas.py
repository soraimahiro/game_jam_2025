import pygame
from vector2 import Vector2
from player import Player
from entity import Entity
from stage import Stage, StageOption, TitleOption
from setting import Setting


def draw_unit(screen: pygame.Surface, entity: Player | Entity):
	width = screen.get_width()
	height = screen.get_height()
	center = Vector2(width, height) / 2
	# 共 7 條橫線和 11 條 直線，各分 8 塊和 12 塊
	delta = min((height - 50) / 8, width / 12)
	shift = Vector2(entity.icon.get_width(), entity.icon.get_height()) / 2
	position = center + entity.pos * delta - shift
	screen.blit(entity.icon, position.to_tuple())

def draw_bar(stage: Stage, screen: pygame.Surface):
	heart = pygame.transform.scale(Setting.health_icon, (50, 50))
	for i in range(stage.player.hp):
		screen.blit(heart, (heart.get_width() * 1.1 * i, 0))
	gold = pygame.transform.scale(Setting.money_icon, (50, 50))
	screen.blit(gold, (screen.get_width() - gold.get_width(), 0))
	font = Setting.font(12)
	text = font.render(f"{stage.player.money} ", 0, (0, 0, 0))
	screen.blit(text, (screen.get_width() - gold.get_width() - text.get_width(), gold.get_height() / 2 - text.get_height() / 3))

def draw_title(stage: Stage, screen: pygame.Surface):
	screen.fill((255, 255, 255))
	font = Setting.font(32)
	text = font.render("Our Game", 0, (0, 0, 255), None)
	screen.blit(text, (screen.get_width() * 0.15, screen.get_height() * 0.25))
	font = Setting.font(24)
	text = font.render("Start", 0, (0, 0, 0) if stage.player.pos.y != TitleOption.START.value else (255, 127, 0), None)
	screen.blit(text, (screen.get_width() * 0.15, screen.get_height() * 0.5))
	text = font.render("Setting", 0, (0, 0, 0) if stage.player.pos.y != TitleOption.SETTING.value else (255, 127, 0), None)
	screen.blit(text, (screen.get_width() * 0.15, screen.get_height() * 0.6))
	text = font.render("Credit", 0, (0, 0, 0) if stage.player.pos.y != TitleOption.CREDIT.value else (255, 127, 0), None)
	screen.blit(text, (screen.get_width() * 0.15, screen.get_height() * 0.7))
	text = font.render("Exit", 0, (0, 0, 0) if stage.player.pos.y != TitleOption.EXIT.value else (255, 127, 0), None)
	screen.blit(text, (screen.get_width() * 0.15, screen.get_height() * 0.8))

def draw_setting(screen: pygame.Surface):
	screen.fill((127, 255, 0))
	font = Setting.font(16)
	text = font.render("Here is nothing you can set.", 0, (0, 0, 0), None)
	screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() * 0.5))
	text = font.render("Press Enter to return", 0, (0, 0, 0), None)
	screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() * 0.6))

def draw_credit(screen: pygame.Surface):
	screen.fill((180, 180, 0))
	font = Setting.font(12)
	text = font.render("Credit", 0, (0, 0, 0), None)
	screen.blit(text, (screen.get_width() * 0.15, screen.get_height() * 0.15))
	text = font.render("Press Enter to return", 0, (0, 0, 0), None)
	screen.blit(text, (screen.get_width() * 0.95 - text.get_width(), screen.get_height() * 0.9))

def draw_battle(stage:Stage, screen: pygame.Surface):
	# fill background
	# screen.fill((255, 127, 127))
	screen.fill((251, 219, 147))
	width = screen.get_width()
	height = screen.get_height()
	center = Vector2(width, height) / 2
	road_icon = pygame.transform.scale(pygame.image.load("./resource/image/type_simple/image_map.png"), (15, 15))
	delta = min((height - 50) / 8, width / 12)
	shift = Vector2(road_icon.get_width(), road_icon.get_height()) / 2
	for i in range(-5, 6):
		for j in range(-3, 4):
			pos= Vector2(i, j)
			position = center + pos * delta - shift
			screen.blit(road_icon, position.to_tuple())
	# Draw player
	draw_unit(screen, stage.player)
	# Draw shadows
	for shadow in stage.shadows:
		if not shadow.pos.y == stage.player.pos.y:
			draw_unit(screen, shadow)
	# Draw entities
	for entity in stage.entities:
		draw_unit(screen, entity)
	# Draw hits
	for skill in stage.player.skills:
		for hit in skill.hits:
			draw_unit(screen, hit.entity)
		skill.update(pygame.time.get_ticks())
	# Draw upper bar
	draw_bar(stage, screen)

def draw_boss(stage: Stage, screen: pygame.Surface):
	# fill background
	# screen.fill((255, 0, 0))
	screen.fill((190, 91, 80))
	width = screen.get_width()
	height = screen.get_height()
	center = Vector2(width, height) / 2
	road_icon = pygame.transform.scale(pygame.image.load("./resource/image/type_simple/image_map.png"), (15, 15))
	delta = min((height - 50) / 8, width / 12)
	shift = Vector2(road_icon.get_width(), road_icon.get_height()) / 2
	for i in range(-5, 6):
		for j in range(-3, 4):
			pos= Vector2(i, j)
			position = center + pos * delta - shift
			screen.blit(road_icon, position.to_tuple())
	# Draw player
	draw_unit(screen, stage.player)
	# Draw entities
	for entity in stage.entities:
		draw_unit(screen, entity)
	# Draw hits
	for skill in stage.player.skills:
		for hit in skill.hits:
			draw_unit(screen, hit.entity)
		skill.update(pygame.time.get_ticks())
	# Draw upper bar
	draw_bar(stage, screen)

def draw_win(screen: pygame.Surface):
	screen.fill((127, 127, 0))
	font = Setting.font(32)
	text = font.render("You Win!!", 0, (0, 0, 0), None)
	screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() * 0.15))
	font = Setting.font(12)
	text = font.render("Press Enter to return", 0, (0, 0, 0), None)
	screen.blit(text, (screen.get_width() * 0.95 - text.get_width(), screen.get_height() * 0.9))

def draw_lose(screen: pygame.Surface):
	screen.fill((72, 72, 72))
	font = Setting.font(32)
	text = font.render("You Lose...", 0, (0, 0, 0), None)
	screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() * 0.15))
	font = Setting.font(12)
	text = font.render("Press Enter to return", 0, (0, 0, 0), None)
	screen.blit(text, (screen.get_width() * 0.95 - text.get_width(), screen.get_height() * 0.9))

def draw(stage: Stage, screen: pygame.Surface):
	if stage.stage == StageOption.TITLE:
		draw_title(stage, screen)
	elif stage.stage == StageOption.SETTING:
		draw_setting(screen)
	elif stage.stage == StageOption.CREDITS:
		draw_credit(screen)
	elif stage.stage == StageOption.BATTLE:
		draw_battle(stage, screen)
	elif stage.stage == StageOption.BOSS:
		draw_boss(stage, screen)
	elif stage.stage == StageOption.END:
		if (stage.player.hp > 0):
			draw_win(screen)
		else:
			draw_lose(screen)
