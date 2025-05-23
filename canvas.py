import pygame
from vector2 import Vector2
from player import Player
from entity import Entity
from skill import Skill
from stage import Stage, StageOption, TitleOption, SettingOption
import globals
import os

def draw_unit(screen: pygame.Surface, entity: Player | Entity):
	HP_MAX = 50
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
	page = globals.icon("./resource/image/image_page_start.png", globals.screen_size)
	screen.blit(page, globals.screen_pos)

	button_path    = "./resource/image/startpage/"
	button_start   = os.path.join(button_path, "image_start_0.png")
	button_settings = os.path.join(button_path, "image_settings_0.png")
	button_credit  = os.path.join(button_path, "image_credit_0.png")
	button_exit    = os.path.join(button_path, "image_exit_0.png")
	if stage.player.pos.y == TitleOption.START.value:
		button_start   = os.path.join(button_path, "image_start_1.png")
	if stage.player.pos.y == TitleOption.SETTING.value:
		button_settings = os.path.join(button_path, "image_settings_1.png")
	if stage.player.pos.y == TitleOption.CREDIT.value:
		button_credit  = os.path.join(button_path, "image_credit_1.png")
	if stage.player.pos.y == TitleOption.EXIT.value:
		button_exit    = os.path.join(button_path, "image_exit_1.png")
	button_size = (globals.button_size[0] * 2, globals.button_size[1]) 
	button_space = 10
	index = 0
	button = globals.icon(button_start, button_size)
	button_pos = ((screen.get_width() - button_size[0]) / 2, (screen.get_height() - button_size[1]) / 2 - 50 + (button_size[1] + button_space) * index)
	screen.blit(button, button_pos)
	index += 1
	button_pos = ((screen.get_width() - button_size[0]) / 2, (screen.get_height() - button_size[1]) / 2 - 50 + (button_size[1] + button_space) * index)
	button = globals.icon(button_settings, button_size)
	screen.blit(button, button_pos)
	index += 1
	button_pos = ((screen.get_width() - button_size[0]) / 2, (screen.get_height() - button_size[1]) / 2 - 50 + (button_size[1] + button_space) * index)
	button = globals.icon(button_credit, button_size)
	screen.blit(button, button_pos)
	index += 1
	button_pos = ((screen.get_width() - button_size[0]) / 2, (screen.get_height() - button_size[1]) / 2 - 50 + (button_size[1] + button_space) * index)
	button = globals.icon(button_exit, button_size)
	screen.blit(button, button_pos)

def draw_setting(stage: Stage,screen: pygame.Surface):
	page = globals.icon("./resource/image/image_page_settings.png", globals.screen_size)
	screen.blit(page, globals.screen_pos)
	img_source_path = "./resource/image"
	img_setting_path = os.path.join(img_source_path, "settings")
	bg_icon_path_0 = os.path.join(img_setting_path, "image_character_box_0.png")
	bg_icon_path_1 = os.path.join(img_setting_path, "image_character_box_1.png")
	sound_icon_path_0 = os.path.join(img_setting_path, "image_voice_0.png")
	sound_icon_path_1 = os.path.join(img_setting_path, "image_voice_1.png")
	skin_color_path_0 = os.path.join(img_setting_path, "image_skincolor_0.png")
	skin_color_path_1 = os.path.join(img_setting_path, "image_skincolor_1.png")

	icon_size = 150
	skin_chr_icon = globals.icon(os.path.join(img_source_path, f"{globals.get_player_img()}.png"), (icon_size-20,icon_size-20))
	skin_shadow_icon = globals.icon(os.path.join(img_source_path, f"{globals.get_shadow_img()}.png"), (icon_size-20,icon_size-20))
	player_pos=(stage.player.pos.x,stage.player.pos.y)

	# player_pos=(0, 0) 
	font = globals.font(size = 30)
	if player_pos != (0, SettingOption.SKIN.value):
		skin_color_icon = globals.icon(skin_color_path_0, (icon_size,icon_size))
	else:
		skin_color_icon = globals.icon(skin_color_path_1, (icon_size,icon_size))
	# text = font.render("Skin Color", 0, (0, 0, 0) if player_pos !=(0, SettingOption.SKIN.value) else (255, 127, 0), None)
	skin_color_pos = (screen.get_width() * 0.2, screen.get_height() * 0.3+5)
	screen.blit(skin_color_icon, skin_color_pos)
	
	# player_pos=(0, 1)
	# text = font.render("Sound", 0, (0, 0, 0) if player_pos !=(0, SettingOption.SOUND.value) else (255, 127, 0), None)
	sound_pos = (screen.get_width() * 0.2, screen.get_height() * 0.60)
	if player_pos != (0, SettingOption.SOUND.value):
		sound_icon = globals.icon(sound_icon_path_0, (icon_size,icon_size))
	else:
		sound_icon = globals.icon(sound_icon_path_1, (icon_size,icon_size))
	screen.blit(sound_icon, sound_pos)
	
	# player_pos=(0, 2)
	# text = font.render("Exit", 0, (0, 0, 0) if player_pos != (0,SettingOption.EXIT.value) else (255, 127, 0), None)

	# player_pos=(1, 0)
	skin_bg_pos = (screen.get_width() * 0.45+5, screen.get_height() * 0.3+5)
	shadow_bg_pos = (skin_bg_pos[0]+icon_size+10, skin_bg_pos[1])
	if player_pos != (1, SettingOption.SKIN.value):
		skin_bg_icon = globals.icon(bg_icon_path_0, (icon_size,icon_size))
	else:
		skin_bg_icon = globals.icon(bg_icon_path_1, (icon_size,icon_size))
	screen.blit(skin_bg_icon, skin_bg_pos)
	screen.blit(skin_bg_icon, shadow_bg_pos)
	# skin_icon = globals.icon(globals.player_img, (icon_size-10,icon_size-10))
	screen.blit(skin_chr_icon, (skin_bg_pos[0]+10,skin_bg_pos[1]+10))
	screen.blit(skin_shadow_icon, (shadow_bg_pos[0]+10,shadow_bg_pos[1]+10))
	# player_pos=(1, 1)
	text = font.render(f"{globals.music_volume}%", 0, (0, 0, 0) if player_pos!=(1,1)  else (255, 127, 0), None)
	screen.blit(text, (screen.get_width() * 0.55, screen.get_height() * 0.65))
	
def draw_credit(screen: pygame.Surface):
	page = globals.icon("./resource/image/image_page_credits.png", globals.screen_size)
	screen.blit(page, globals.screen_pos)

def draw_battle(stage:Stage, screen: pygame.Surface):
	# fill background
	# screen.fill((255, 127, 127))
	screen.fill((247, 248, 190))
	width = screen.get_width()
	height = screen.get_height()
	center = Vector2(width, height) / 2
	road_icon = globals.icon("./resource/image/type_simple/image_map_battle.png", (75, 75))
	delta = min((height - 50) / 8, width / 12)
	shift = Vector2(road_icon.get_width(), road_icon.get_height()) / 2
	for i in range(-5, 6):
		for j in range(-3, 4):
			pos= Vector2(i, j)
			position = center + pos * delta - shift
			screen.blit(road_icon, position.to_tuple())
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
	# Draw shadows
	for shadow in stage.shadows:
		if not shadow.pos.y == stage.player.pos.y:
			draw_unit(screen, shadow)
	# Draw player
	draw_unit(screen, stage.player)

def draw_boss(stage: Stage, screen: pygame.Surface):
	# fill background
	# screen.fill((255, 0, 0))
	screen.fill((190, 91, 80))
	width = screen.get_width()
	height = screen.get_height()
	center = Vector2(width, height) / 2
	road_icon = globals.icon("./resource/image/type_simple/image_map.png", (75, 75))
	delta = min((height - 50) / 8, width / 12)
	shift = Vector2(road_icon.get_width(), road_icon.get_height()) / 2
	for i in range(-5, 6):
		for j in range(-3, 4):
			pos= Vector2(i, j)
			position = center + pos * delta - shift
			screen.blit(road_icon, position.to_tuple())
	# Draw entities
	for entity in stage.entities:
		if entity.type in {Entity.T_BOSS, Entity.T_MONSTER} and entity.hp <= 0: ...
		else:
			draw_unit(screen, entity)
	# Draw hits
	for skill in stage.player.skills:
		for hit in skill.hits:
			draw_unit(screen, hit.entity)
		skill.update(pygame.time.get_ticks())
	# Draw upper bar
	draw_bar(stage, screen)
	# Draw player
	draw_unit(screen, stage.player)
	

def draw_win(screen: pygame.Surface):
	page = globals.icon("./resource/image/image_page_win.png", globals.screen_size)
	screen.blit(page, globals.screen_pos)

def draw_lose(screen: pygame.Surface):
	page = globals.icon("./resource/image/image_page_lose.png", globals.screen_size)
	screen.blit(page, globals.screen_pos)

def draw_esc_menu(stage: Stage, screen: pygame.Surface):
	rect_x = (screen.get_width() - 400) // 2
	rect_y = (screen.get_height() - 300) // 2
	background = globals.icon("./resource/image/esc_menu/image_esc_beckground.png", (400, 300))
	screen.blit(background, (rect_x, rect_y))
	button_path    = "./resource/image/esc_menu/"
	button_continue = os.path.join(button_path, "image_esc_continue_0.png")
	button_settings = os.path.join(button_path, "image_esc_settings_0.png")
	button_back     = os.path.join(button_path, "image_esc_back_0.png")
	if stage.esc_menu.option == 0:
		button_continue = os.path.join(button_path, "image_esc_continue_1.png")
	if stage.esc_menu.option == 1:
		button_settings = os.path.join(button_path, "image_esc_settings_1.png")
	if stage.esc_menu.option == 2:
		button_back = os.path.join(button_path, "image_esc_back_1.png")

	button_size_x = 210
	button_size_y = 70
	button = globals.icon(button_continue, (button_size_x, button_size_y))
	screen.blit(button, ((screen.get_width() - button_size_x) / 2, rect_y + 22.5 ))
	button = globals.icon(button_settings, (button_size_x, button_size_y))
	screen.blit(button, ((screen.get_width() - button_size_x) / 2, rect_y + button_size_y + 22.5 * 2 ))
	button = globals.icon(button_back, (button_size_x, button_size_y))
	screen.blit(button, ((screen.get_width() - button_size_x) / 2, rect_y + button_size_y * 2 + 22.5 * 3 ))


def draw_shop(stage: Stage, screen: pygame.Surface) -> bool:
	size = Vector2(screen.get_width() * 5 // 7, screen.get_height() * 5 // 7)
	rect = (Vector2(screen.get_width(), screen.get_height()) - size) // 2
	background = globals.icon("./resource/image/esc_menu/image_esc_beckground.png", size.to_tuple())
	screen.blit(background, rect.to_tuple())
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
		good_icon = globals.icon(f"./resource/image/shop/image_skill_{the_type}_{1 if stage.shop_info.option == i else 0}.png", (128, 128))
		cost_icon = globals.icon("./resource/image/type_simple/image_money.png")
		cost_text = globals.font(size = 16).render(f"{stage.player.skills[no].cost()}", 0, (80, 11, 52))
		the_level = stage.player.skills[no].level
		level_icon = globals.icon(f"./resource/image/shop/image_skill_level_{the_level if the_level in range(3) else 'max'}.png")
		pos = Vector2(screen.get_width() // 2, screen.get_height() // 2) + Vector2(screen.get_width() // 5, 0) * (i - 1)
		screen.blit(good_icon, (pos - Vector2(good_icon.get_width() // 2, good_icon.get_height() // 2)).to_tuple())
		screen.blit(cost_icon, (pos - Vector2(0, screen.get_height() // 9) - Vector2(cost_icon.get_width() // 2, cost_icon.get_height() // 2)).to_tuple())
		screen.blit(cost_text, (pos - Vector2(0, screen.get_height() // 6) - Vector2(cost_text.get_width() // 2, cost_text.get_height() // 2)).to_tuple())
		screen.blit(level_icon, (pos + Vector2(0, screen.get_height() // 9) - Vector2(level_icon.get_width() // 2, level_icon.get_height() // 2)).to_tuple())
	return True

def draw_story(stage: Stage, screen: pygame.Surface):
	# print(f"draw_story: {stage.story_count}")
	if globals.story_list[stage.story_count] == 0:
		print("error in draw_story")
		return
	page = globals.icon(globals.story_list[stage.story_count], globals.screen_size)
	screen.blit(page, globals.screen_pos)

def draw(stage: Stage, screen: pygame.Surface):
	if stage.stage == StageOption.TITLE:
		draw_title(stage, screen)
	elif stage.stage == StageOption.SETTING:
		draw_setting(stage,screen)
	elif stage.stage == StageOption.CREDITS:
		draw_credit(screen)
	elif stage.stage == StageOption.BATTLE_STORY or stage.stage == StageOption.BOSS_STORY:
		draw_story(stage, screen)
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