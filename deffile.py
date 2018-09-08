def cars(made,types,**other):
	car={}
	car['made']=made
	car['type']=types
	for key,value in other.items():
		car[key]=value
	return car