def div69by(no):
	try: 
		return 69/no	
	except ZeroDivisionError:
		print('Error: You cannot divide a no by 0')		
		
print(div69by(10))
print(div69by(69))
print(div69by(0))
print(div69by(2))
