import pygame

class Setting:
	player_icon = pygame.image.load("./resource/image/type_simple/image_character_blue.png")
	health_icon = pygame.image.load("./resource/image/type_simple/image_HP.png")
	money_icon = pygame.image.load("./resource/image/type_simple/image_money.png")
	shadow_img = "emerald"
	font_scale = 4
	icon_size = (50, 50)
	def font(size: int):
		return pygame.font.SysFont("NOTOSANSTC-VARIABLEFONT_WGHT.TTF", size * Setting.font_scale)