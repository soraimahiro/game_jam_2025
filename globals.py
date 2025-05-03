import pygame

def init():
	global step_moved
	step_moved = 0
	global enemy_killed
	enemy_killed = 0	
	global player_icon
	player_icon = pygame.image.load("./resource/image/type_simple/image_character_blue.png")
	global health_icon
	health_icon = pygame.image.load("./resource/image/type_simple/image_HP.png")
	global money_icon
	money_icon = pygame.image.load("./resource/image/type_simple/image_money.png")
	global font_scale
	font_scale = 4
	global font_file
	font_file = "NOTOSANSTC-VARIABLEFONT_WGHT.TTF"
	global shadow_img
	shadow_img = "emerald"
	global icon_size
	icon_size = (50, 50)
	