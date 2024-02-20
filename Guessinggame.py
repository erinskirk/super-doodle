# This is a guess the number game
import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

#Ask the player to guess 6 times
for guessesTaken in range (1,7):
	print('Guess # ' + str(guessesTaken) + '. Take a guess')
	guess = int(input())
	
	
	if guess < secretNumber:
		print ('Your guess was too low')
	elif guess > secretNumber:
		print ('Your guess was too high')
	else:
		break #this is the correct guess
if guess == secretNumber:
	print('Good job you guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
	print ('Nope. The number I was thinking of was ' + str(secretNumber))
input('Confirm by pressing any key')