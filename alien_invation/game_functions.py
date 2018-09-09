import sys
import pygame
from bullet import Bullet
from alien import Alien

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

def check_events(ai_settings,screen,ship,bullets):
	"""响应鼠标键盘"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)

def fire_bullet(ai_settings,screen,ship,bullets):
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet=Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)

def update_screen(ai_settings,screen,ship,aliens,bullets):
	"""让最近绘制的屏幕可见"""
	screen.fill(ai_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	aliens.draw(screen)
	pygame.display.flip()

def update_bullets(aliens,bullets):
	"""更新子弹的位置，删除已经消失的子弹"""
	bullets.update()
		# 删除消失子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	collisions=pygame.sprite.groupcollide(bullets,aliens,True,True)

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

def update_aliens(ai_settings,aliens):
	"""检查是否有外星人在边缘，并调整位置"""
	check_fleet_edges(ai_settings,aliens)
	aliens.update()
