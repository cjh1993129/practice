class GameStats():
	"""跟踪游戏统计信息"""
	def __init__(self,ai_settings):
		""" 初始化"""
		self.ai_settings=ai_settings
		self.reset_stats()
		# 游戏启动
		self.game_active=False
	def reset_stats(self):
		"""初始化可能变化的统计信息"""
		self.ships_left=self.ai_settings.ship_limit
		self.score=0