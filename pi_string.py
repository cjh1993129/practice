filename="pi_million_digits.txt"
with open(filename) as file_object:
	lines=file_object.readlines()
pi_string=''
for line in lines:
	pi_string += line.rstrip()

birthday=input('birthday')
if birthday in pi_string:
	print('1')
else:
	print('2')

print(pi_string[:52])
print(len(pi_string))