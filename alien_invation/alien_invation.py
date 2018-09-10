import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
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
	# 创建PLAY按钮
	play_button=Button(ai_settings,screen,"Play")
	# 创建飞船、子弹、外星人
	ship=Ship(ai_settings,screen)
	bullets=Group()
	aliens=Group()
	# 创建记分牌
	stats=GameStats(ai_settings)
	sb=Scoreboard(ai_settings,screen,stats)
	gf.create_fleet(ai_settings,screen,ship,aliens)

	# 开始游戏的主循环
	while True:
		# 监视鼠标和键盘
		gf.check_events(ai_settings,screen,stats,play_button,ship,
			aliens,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
		# 更新屏幕
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
			play_button)	
run_game()