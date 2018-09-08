filename='learning_python.txt'
with open(filename,'a') as file:
	name=input('name')
	print('hello '+name) 
	file.write(name+' has came here.')

		