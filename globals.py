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
	shadow_img = "type_simple/image_shadow_blue"
	global icon_size
	icon_size = (50, 50)
icon_set: set[tuple[str, tuple[int, int], pygame.Surface]] = set()
def icon(img: str, size: tuple[int, int] = None):
	if size == None:
		size = icon_size
	for icon in icon_set:
		if icon[0] == img and icon[1] == size:
			return icon[2]
	new = pygame.transform.scale(pygame.image.load(img), size)
	icon_set.add((img, size, new))
	return new
