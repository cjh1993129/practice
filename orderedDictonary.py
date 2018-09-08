from random import randint
class Die():
	def __init__(self,sides=6):
		self.sides=sides

	def roll_die(self,a=10):
		while a>0:
			x=randint(1,self.sides)
			print(x)
			a=a-1
roll=Die()
roll.roll_die(10)
roll.roll_die(20)
roll.roll_die(30)

