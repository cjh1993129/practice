import json
def number():
	filename='number.json'
	try:
		with open(filename) as f:
			number=json.load(f)
	except FileNotFoundError:
		number=input('your number:')
		with open(filename,'w') as f:
			json.dump(number,f)
		print('stored')
	else:
		print('favourite number: '+number)
number()