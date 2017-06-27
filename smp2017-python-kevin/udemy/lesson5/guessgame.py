#game pgm to guess a number b/w 1 and 40

import random

print('What is your name, human?')
name = input()
print('Yo '+name+', guess a number between 1 and 40')

ans = random.randint(1,40)

#max chances to guess is 8

for totguess in range(1,9):
	print('Your guess?')
	guess = int(input())

	if(guess<1 or guess> 40):
		print('BRUH. That is not even the range, man')
	elif(guess>ans):
		print('Guess is too high')
	elif(guess<ans):
		print('Guess is too low')	
	else:
		break #counts no of guess

if(ans == guess):
	print('Damn son. You guessed the number '+ str(totguess) + ' times')
else:
	print('Too bad. The no which you could not guess was ' + str(ans))

