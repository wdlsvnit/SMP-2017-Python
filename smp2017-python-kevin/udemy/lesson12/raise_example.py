'''
*********
*	*
*	*
*	*
*	*
*********
'''

print('Enter symbol:')
symbol = input()

print('Enter width:')
width = input()

print('Enter height:')
height = input()

def Box(symbol,width,height):
	if(len(symbol)!=1):
		raise Exception('symbol length should be 1')
	if(width<2) or (height<2):
		raise Exception('Width & Height should be greater 1')	
	print(symbol*width)
	for i in range(height-2):
		print(symbol + ' '*(width-2) + symbol)
	print(symbol*width)

Box(symbol,int(width),int(height))
