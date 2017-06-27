print('How many dogs do you have?')

Dog=input()

try:
	if(int(Dog)>3):
		print('that is a lot of dogs')
	elif(int(Dog)<0):
		print('how the hell do you have negative number of dogs')
	else:
		print('not a lot of dogs')
		

except ValueError:
	print('Enter valid number')


