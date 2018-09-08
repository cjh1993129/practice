class Res():
	def __init__(self,res_name,cuisine_type):
		self.res_name=res_name
		self.cuisine_type=cuisine_type
	def de_res(self):
		print(self.res_name+':\t'+self.cuisine_type)
	def open_res(self):
		print('opening')

