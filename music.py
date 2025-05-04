import pygame
import os
import globals
def play_background_music(stage):
	from stage import StageOption  # 延遲導入以避免循環導入
	if stage.stage == StageOption.TITLE:
		bgm_file = "bgm_menu_DustyRoadMagic.mp3"
	elif stage.stage == StageOption.SETTING:
		bgm_file = "bgm_menu_LastCappuccinoInRio.mp3"
	elif stage.stage == StageOption.BATTLE:
		bgm_file = "bgm_mob_Matterhorn.mp3"
	elif stage.stage == StageOption.BOSS:
		bgm_file = "bgm_boss_Future.mp3"
	elif stage.stage == StageOption.END:
		bgm_file = "bgm_menu_TreasureHunt.mp3"
	elif stage.stage == StageOption.CREDITS:
		# todo: add credits music
		bgm_file = "bgm_menu_DustyRoadMagic.mp3"
		pass
	elif stage.stage == StageOption.SHOP:
		bgm_file = "bgm_shop_SunriseFromAMoonbeam.mp3"
	else:
		return
	pygame.mixer.music.load(os.path.join(globals.music_file_path, bgm_file))
	pygame.mixer.music.play(-1)

def change_music_volume(volume:int):
	pygame.mixer.music.set_volume(volume / 100)

def play_sound_effect(sound_name:str):
	# sound_path = "./resource/sound/"
	sound_file = f"sound_{sound_name}.mp3"
	sound = pygame.mixer.Sound(os.path.join(globals.sound_file_path, sound_file))
	sound.set_volume(globals.sound_volume / 100)
	sound.play()