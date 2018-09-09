import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
	"""初始化游戏，创建对象"""
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption('Alien Invasion')
	# 创建飞船、子弹、外星人
	ship=Ship(ai_settings,screen)
	bullets=Group()
	aliens=Group()
	gf.create_fleet(ai_settings,screen,ship,aliens)

	# 开始游戏的主循环
	while True:
		# 监视鼠标和键盘
		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		gf.update_bullets(aliens,bullets)
		gf.update_screen(ai_settings,screen,ship,aliens,bullets)	
		gf.update_aliens(ai_settings,aliens)
run_game()