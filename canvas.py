import pygame
from vector2 import Vector2
from player import Player
from entity import Entity
from skill import Skill
from stage import Stage, StageOption, TitleOption
import globals

def draw_unit(screen: pygame.Surface, entity: Player | Entity):
	HP_MAX = 18
	width = screen.get_width()
	height = screen.get_height()
	center = Vector2(width, height) / 2
	# 共 7 條橫線和 11 條 直線，各分 8 塊和 12 塊
	delta = min((height - 50) / 8, width / 12)
	icon = entity.icon()
	shift = Vector2(icon.get_width(), icon.get_height()) / 2
	position = center + entity.pos * delta - shift
	screen.blit(icon, position.to_tuple())
	if isinstance(entity, Entity):
		if (entity.type == Entity.T_MONSTER or entity.type == Entity.T_BOSS) and entity.hp > 0:
			if entity.hp <= HP_MAX:
				hp_icon = globals.icon(f"./resource/image/type_simple/image_hp_{entity.hp}.png", (30, 30))
			else:
				hp_icon = globals.icon(f"./resource/image/type_simple/image_hp_large.png", (30, 30))
			screen.blit(hp_icon, position.to_tuple())

def draw_bar(stage: Stage, screen: pygame.Surface):
	heart = globals.icon(globals.health_img)
	for i in range(stage.player.hp):
		screen.blit(heart, (heart.get_width() * 1.1 * i, 0))
	gold = globals.icon(globals.money_img)
	screen.blit(gold, (screen.get_width() - gold.get_width(), 0))
	font = globals.font(size = 12)
	text = font.render(f"{stage.player.money} ", 0, (0, 0, 0))
	screen.blit(text, (screen.get_width() - gold.get_width() - text.get_width(), gold.get_height() / 2 - text.get_height() / 3))
	if stage.stage == StageOption.BATTLE:
		step = globals.icon(globals.step_img)
		screen.blit(step, (screen.get_width() - gold.get_width(), screen.get_height() - gold.get_height()))
		text = font.render(f"{stage.round_pass}/{stage.boss_wait} ", 0, (0, 0, 0))
		screen.blit(text, (screen.get_width() - gold.get_width() - text.get_width(), screen.get_height() - gold.get_height() / 2 - text.get_height() / 3))

def draw_title(stage: Stage, screen: pygame.Surface):
	screen.fill((255, 255, 255))
	font = globals.font(size = 32)
	text = font.render("Our Game", 0, (0, 0, 255), None)
	screen.blit(text, (screen.get_width() * 0.15, screen.get_height() * 0.25))
	font = globals.font(size = 24)
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
	font = globals.font(size = 16)
	text = font.render("Here is nothing you can set.", 0, (0, 0, 0), None)
	screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() * 0.5))
	text = font.render("Press Enter to return", 0, (0, 0, 0), None)
	screen.blit(text, (screen.get_width() / 2 - text.get_width() / 2, screen.get_height() * 0.6))

def draw_credit(screen: pygame.Surface):
	screen.fill((180, 180, 0))
	font = globals.font(size = 12)
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
	road_icon = globals.icon("./resource/image/type_simple/image_map.png", (15, 15))
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
	road_icon = globals.icon("./resource/image/type_simple/image_map.png", (15, 15))
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
	page = globals.icon("./resource/image/image_page_win.png", (800, 600))
	screen.blit(page, (0, 0))

def draw_lose(screen: pygame.Surface):
	page = globals.icon("./resource/image/image_page_lose.png", (800, 600))
	screen.blit(page, (0, 0))

def draw_esc_menu(stage: Stage, screen: pygame.Surface):
	rect_width, rect_height = 400, 300
	rect_x = (screen.get_width() - rect_width) // 2
	rect_y = (screen.get_height() - rect_height) // 2
	pygame.draw.rect(screen, (255, 255, 255), (rect_x, rect_y, rect_width, rect_height))
	font = globals.font(size = 16)
	text = font.render("Continue", 0, (255, 127, 0) if stage.esc_menu.option == 0 else (0, 0, 0), None)
	screen.blit(text, (rect_x + 50, screen.get_height() / 2 - 50))
	text = font.render("Back to Title", 0, (255, 127, 0) if stage.esc_menu.option == 1 else (0, 0, 0), None)
	screen.blit(text, (rect_x + 50, screen.get_height() / 2 + 10))	

def draw_shop(stage: Stage, screen: pygame.Surface) -> bool:
	rect = pygame.Rect(screen.get_width() // 7, screen.get_height() // 7, screen.get_width() * 5 // 7, screen.get_height() * 5 // 7)
	pygame.draw.rect(screen, (255, 255, 255), rect, screen.get_width() * 3 // 5)
	for i in range(3):
		no = -1
		for j in range(stage.player.skills.__len__()):
			if stage.player.skills[j].attacktype == stage.shop_info.goods[i]:
				no = j
				break
		if no == -1:
			no = stage.player.skills.__len__()
			stage.player.skills.append(Skill(1, 0, stage.shop_info.goods[i]))
		the_type = stage.shop_info.goods[i].__repr__()
		the_type = the_type[the_type.find('.') + 1:the_type.rfind(':')]
		if stage.shop_info.option == i:
			sell = Entity(f"shop/image_skill_{the_type}_1", Entity.T_GOODS, -1, 0, Vector2(i * 3 - 3, 0), Vector2(0, 0), 0, 1, 0)
		else:
			sell = Entity(f"shop/image_skill_{the_type}_0", Entity.T_GOODS, -1, 0, Vector2(i * 3 - 3, 0), Vector2(0, 0), 0, 1, 0)
		cost = Entity("type_simple/image_money", Entity.T_DISPLAY, -1, 0, Vector2(i * 3 - 3, -1), Vector2(0, 0), 0, 1, 0)
		level = Entity(f"shop/image_skill_level_{stage.player.skills[no].level}", Entity.T_DISPLAY, -1, 0, Vector2(i * 3 - 3, 1), Vector2(0, 0), 0, 1, 0)
		draw_unit(screen, sell)
		draw_unit(screen, cost)
		draw_unit(screen, level)
	return True

def draw_story(screen: pygame.Surface):
	screen.fill((251, 219, 147))
	font = globals.font(size = 16)
	text = font.render("sadasddassd\ndsadasdasd\nasadasda", 0, (0, 0, 0), None)
	screen.blit(text, (50, 50))

def draw(stage: Stage, screen: pygame.Surface):
	if stage.stage == StageOption.TITLE:
		draw_title(stage, screen)
	elif stage.stage == StageOption.SETTING:
		draw_setting(screen)
	elif stage.stage == StageOption.CREDITS:
		draw_credit(screen)
	elif stage.stage == StageOption.BATTLE_STORY:
		draw_story(screen)
	elif stage.stage == StageOption.BATTLE:
		draw_battle(stage, screen)
	elif stage.stage == StageOption.SHOP:
		draw_shop(stage, screen)
	elif stage.stage == StageOption.BOSS:
		draw_boss(stage, screen)
	elif stage.stage == StageOption.END:
		if (stage.player.hp > 0):
			draw_win(screen)
		else:
			draw_lose(screen)
	
	if stage.esc_menu.show:
		draw_esc_menu(stage, screen)
