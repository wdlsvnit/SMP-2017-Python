import re

ph=re.compile(r'\d\d\d\d\d\d\d\d')

lol = (ph.findall('call me at 23718549 or 99724767'))

for i in range(len(lol)):
	print('Number '+str(i+1)+': '+ lol[i])

