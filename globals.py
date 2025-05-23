import pygame
import pygame.image
from os.path import exists

def init():
	global step_moved
	step_moved = 0
	global enemy_killed
	enemy_killed = 0
	global icon_size
	icon_size = (50, 50)
	global button_size
	button_size = (75, 75)
	global goods_size
	goods_size = (125, 125)
	global screen_size
	screen_size = (800, 600)
	global screen_pos
	screen_pos = (0, 0)
	global color
	color = ["blue", "gray","green","purple","red","yellow"]
	global color_index
	color_index = 0
	global player_img
	player_img = get_player_img()
	global health_img
	health_img = "./resource/image/type_simple/image_HP.png"
	global money_img
	money_img = "./resource/image/type_simple/image_money.png"
	global step_img
	step_img = "./resource/image/type_simple/image_step.png"
	global font_scale
	font_scale = 4
	global font_file
	font_file = "NOTOSANSTC-VARIABLEFONT_WGHT.TTF"
	global shadow_img
	shadow_img = get_shadow_img()
	global music_volume
	music_volume = 10
	global sound_volume
	sound_volume = music_volume
	global music_file_path
	music_file_path = "./resource/bgm/"
	global sound_file_path
	sound_file_path = "./resource/sound/"
	global story_list
	story_list = [
		"./resource/image/story/image_story_0.png",
		"./resource/image/story/image_story_1_1.png",
		"./resource/image/story/image_story_1_2.png",
		"./resource/image/story/image_level_1_1.png",
		0,
		"./resource/image/story/image_story_2.png",
		"./resource/image/story/image_level_1_2.png",
		0,
		"./resource/image/story/image_level_2_1.png",
		0,
		"./resource/image/story/image_level_2_2.png",
		0,
		"./resource/image/story/image_level_3_1.png",
		0,
		"./resource/image/story/image_level_3_2.png",
		0,
		"./resource/image/story/image_level_4_1.png",
		0,
		"./resource/image/story/image_level_4_2.png",
		0,
	]


def get_player_img():
	return f"type_simple/image_character_{color[color_index]}"

def get_shadow_img():
	return f"type_simple/image_shadow_{color[color_index]}"

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
	if exists(img):
		new = pygame.transform.scale(pygame.image.load(img), size).convert_alpha()
	else:
		print(f"{img} not exists")
		new = pygame.transform.scale(pygame.image.load("./resource/image/error.png"), size).convert_alpha()
	icon_set.add((img, size, new))
	return new.copy()
