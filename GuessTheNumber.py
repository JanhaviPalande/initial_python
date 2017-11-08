import random
x = random.randrange(1,21)
t=1
while(t):
	y = int(input('Guess the number: '))
	if x == y:
		print('Correct guess! congrats!')
		t = 0
	else:
		if x > y:
			print('Too low. Try again')
		else:
			print('Too high. Try again')
