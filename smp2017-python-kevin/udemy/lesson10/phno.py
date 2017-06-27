#pgm that checks phno is valid eg:415-555-0000

def phno(no):
	if(len(no)!=12):
		return False 		#max 12 characters
	
	for i in range(0,3):
		if not(no[i].isdecimal()):
			return False	#first 3 should be no:es 

	if(no[3]!='-'):
		return False
	
	for i in range(4,7):
		if not(no[i].isdecimal()):
			return False	 

	
	if(no[7]!='-'):
		return False
	
	for i in range(8,12):
		if not(no[i].isdecimal()):
			return False	 
	return True


message = 'yo call me at either 123-342-3144 or 131-313-3524'

f=0

for i in range(len(message)):
	part = message[i:i+12]
	if(phno(part)==True):
		print('number found: '+part)
		f=1
if(f==0):
	print('no number found')
		
	






