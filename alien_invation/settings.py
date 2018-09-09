class Settings():
	"""游戏设置的类"""
	def __init__(self):
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(255,255,255)
		# 飞船设置
		self.ship_limit=3
		self.ship_speed_factor = 1.3
		# 子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = 255,0,0
		self.bullet_allowed = 3
		# 外星人设置
		self.alien_speed_factor= 0.2
		self.fleet_drop_speed =100
		self.fleet_direction=1
