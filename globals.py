import pygame
import pygame.image

def init():
	global step_moved
	step_moved = 0
	global enemy_killed
	enemy_killed = 0
	global icon_size
	icon_size = (50, 50)
	global player_icon
	player_icon = icon("./resource/image/type_simple/image_character_blue.png")
	global health_icon
	health_icon = icon("./resource/image/type_simple/image_HP.png")
	global money_icon
	money_icon = icon("./resource/image/type_simple/image_money.png")
	global font_scale
	font_scale = 4
	global font_file
	font_file = "NOTOSANSTC-VARIABLEFONT_WGHT.TTF"
	global shadow_img
	shadow_img = "type_simple/image_shadow_blue"

font_set: set[tuple[str, int, pygame.font.Font]] = set()
def font(file: str = None, size: int = 8, scale = None, bold: bool = False, italic: bool = False):
	if file == None:
		file = font_file
	if scale == None:
		scale = font_scale
	for font in font_set:
		if font[0] == file and font[1] == size * scale:
			return font[2]
	new = pygame.font.SysFont(file, size * scale, bold, italic)
	font_set.add((file, size * scale, new))
	return new

icon_set: set[tuple[str, tuple[int, int], pygame.Surface]] = set()
def icon(img: str, size: tuple[int, int] = None):
	if size == None:
		size = icon_size
	for icon in icon_set:
		if icon[0] == img and icon[1] == size:
			return icon[2].copy()
	new = pygame.transform.scale(pygame.image.load(img), size).convert_alpha()
	icon_set.add((img, size, new))
	return new.copy()
