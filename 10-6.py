import json
def loadfile():
	filename='username.json'
	try:
		with open(filename) as f:
			username=json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username

def buildname():
	username=input('name:    ')
	filename = 'username.json'
	with open(filename,'w') as f:
		json.dump(username,f)
	return username

def greet():
	username=loadfile()
	if username:
		print('welcome '+username)
	else:
		username=buildname()
		print('remember you '+username)
greet()
