import pygame

def init():
    global step_moved
    global enemy_killed
    global player_icon
    global health_icon
    global money_icon
    global font_scale
    global font_file

    step_moved = 0
    enemy_killed = 0	
    player_icon = pygame.image.load("./resource/image/type_simple/image_character_blue.png")
    health_icon = pygame.image.load("./resource/image/type_simple/image_HP.png")
    money_icon = pygame.image.load("./resource/image/type_simple/image_money.png")
    font_file = "NOTOSANSTC-VARIABLEFONT_WGHT.TTF"
    font_scale = 4