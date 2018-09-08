def countwords(filename):
	try:
		with open(filename) as a:
			content=a.read()
			print(content)
	except FileNotFoundError:
		pass
	else:
		words=content.split()
		num=len(words)
		print(str(num)+' words.')
filename='alice.txt'
filename2='sa.txt'
countwords(filename)
countwords(filename2)