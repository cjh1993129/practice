import pygame.font

class Scoreboard():
	"""得分"""
	def __init__(self,ai_settings,screen,stats):
		"""初始化得分"""
		self.screen=screen
		self.screen_rect=screen.get_rect()
		self.ai_settings=ai_settings
		self.stats=stats
		"""字体设置"""
		self.text_color=(30,30,30)
		self.font=pygame.font.SysFont(None,48)
		"""初始得分图像"""
		self.prep_score()
	def prep_score(self):
		"""将得分转换为图像"""
		score_str=str(self.stats.score)
		self.score_image=self.font.render(score_str,True,self,text_color,
			self.ai_settings.bg_color)
		# 得分放在左上角
		self.score_rect=self.score_image.get_rect()
		self.score_rect.right=self.screen_rect.right-20
		self.score_rect.top=20
	def show_score(self):
		"""显示得分"""
		self.screen.blit(self.score_image,self.score_rect)
