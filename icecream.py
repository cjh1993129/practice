from restaurant import Res
class IceCream(Res):
	def __init__(self,res_name,cuisine_type):
		super().__init__(res_name,cuisine_type)
		self.flavos=['apple','peach','pear']
	def show_ice(self):
		for flavo in self.flavos:
			print(flavo+' icecream')