class Settings():
	"""游戏设置的类"""
	def __init__(self):
		"""静态设置"""
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(255,255,255)
		# 飞船设置
		self.ship_limit=2
		self.ship_speed_factor = 1.3
		# 子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 255,0,0
		self.bullet_allowed = 3
		# 外星人设置
		self.alien_speed_factor= 0.1
		self.fleet_drop_speed = 5
		self.fleet_direction=1
		# 游戏节奏加快
		self.speedup_scale=1.1
		self.initialize_dynamic_settings()
	def initialize_dynamic_settings(self):
		"""游戏变化设置"""
		self.ship_speed_factor=1.5
		self.bullet_speed_factor=3
		self.alien_speed_factor=0.5
		# 1右-1左
		self.fleet_direction=1
	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
