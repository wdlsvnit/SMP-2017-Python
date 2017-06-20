#pgm that counts number of each letter in a sentence	

import pprint

print('Enter sentence: ')
sentence = input()

req = {}

for ch in sentence.lower():
	req.setdefault(ch,0)
	req[ch]+=1

pprint.pprint(req)
