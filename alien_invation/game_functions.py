import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
def check_keydown_events(event,ai_settings,screen,ship,bullets):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_RIGHT:
			ship.moving_right=True
		elif event.key == pygame.K_LEFT:
			ship.moving_left=True
		elif event.key == pygame.K_SPACE:
		# 创建子弹，并加入编组bullets中
			fire_bullet(ai_settings,screen,ship,bullets)
		elif event.key == pygame.K_q:
			sys.exit()
def check_keyup_events(event,ship):
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_RIGHT:
			ship.moving_right=False
		elif event.key == pygame.K_LEFT:
			ship.moving_left=False

def check_events(ai_settings,screen,stats,play_button,ship,aliens,
	bullets):
	"""响应鼠标键盘"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y =pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,play_button,ship,
				aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_settings,screen,stats,play_button,ship,
	aliens,bullets,mouse_x,mouse_y):
	"""单击开始游戏"""
	button_click=play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_click and not stats.game_active:
		# 重置游戏设置
		ai_settings.initialize_dynamic_settings()
		# 隐藏光标
		pygame.mouse.set_visible(False)
		# 重置游戏
		stats.reset_stats()
		stats.game_active=True

		# 清空工外星人、子弹
		aliens.empty()
		bullets.empty()

		# 创建新的外星人，飞船居中
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()

def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet=Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)

def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
	play_button):
	"""更新屏幕"""
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	# 显示得分
	sb.show_score()
	# 非活动，就显示play
	if not stats.game_active:
		play_button.draw_button()
	# 最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
	"""更新子弹的位置，删除已经消失的子弹"""
	bullets.update()
	# 删除消失子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings,screen,ship,aliens,
		bullets)

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,
	bullets):
	"""子弹击中，则删除子弹和外星人"""
	collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)
	if len(aliens) == 0:
		# 删除现有子弹，加快游戏节奏
		bullets.empty()
		ai_settings.increase_speed()
		create_fleet(ai_settings,screen,ship,aliens)

def get_number_aliens_x(ai_settings,alien_width):
	"""计算每行多少个外星人"""
	available_space_x=ai_settings.screen_width-2*alien_width
	number_aliens_x=int(available_space_x/(2*alien_width))
	return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	"""创建一个外星人放在当前行"""
	alien=Alien(ai_settings,screen)
	alien_width=alien.rect.width
	alien.x=alien_width+2*alien_width*alien_number
	alien.rect.x=alien.x
	alien.rect.y=alien.rect.height+2*alien.rect.height*row_number
	aliens.add(alien)

def create_fleet(ai_settings,screen,ship,aliens):
	"""创建外星人群"""
	alien=Alien(ai_settings,screen)
	number_aliens_x=get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows=get_number_rows(ai_settings,ship.rect.height,
		alien.rect.height)
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,
				row_number)

def get_number_rows(ai_settings,ship_height,alien_height):
	"""计算可以容纳多少行外星人"""
	available_space_y=(ai_settings.screen_height-(3*alien_height)-
		ship_height)
	number_rows=int(available_space_y/(2*alien_height))
	return number_rows
def check_fleet_edges(ai_settings,aliens):
	"""外星人到达边缘时采取相应措施"""
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break
def change_fleet_direction(ai_settings,aliens):
	"""下移外星人，改变方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1


def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
	"""响应被撞到的飞船"""
	# 飞船数量减1
	if stats.ships_left > 0:
		stats.ships_left -= 1
		# 清空外星人、子弹
		aliens.empty()
		bullets.empty()
		# 创建新的外星人和飞船
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()
		#暂停
		sleep(0.5)
	else:
		stats.game_active=False 
		pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
	"""检查是否有外星人到达底部"""
	screen_rect=screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
			break

def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
	"""检查是否有外星人在边缘，并调整位置"""
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
	# 检测外星人和飞船的碰撞
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
	check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)
