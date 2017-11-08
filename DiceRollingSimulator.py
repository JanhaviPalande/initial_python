import random
y=1
while(y):
	x = random.randrange(1,7)
	print(x)
	print('Continue?')
	c = input('Press (y/n)')
	if c !='y' :
		y = 0
