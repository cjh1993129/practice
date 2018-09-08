def conutthe(filename):
	try:
		with open(filename,encoding='utf-8') as fn:
			contents=fn.read()
	except FileNotFoundError:
		pass
	else:
		number=contents.lower().count('the')
		print(number)
filenames=['57857-0.txt','57860-0.txt','pg57850.txt']
for filename in filenames:
	conutthe(filename)