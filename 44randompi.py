import random

i1 = 0
i2 = 0
while True:
	i1 = i1 + 1
	x = random.random()
	y = random.random()
	z = (x**2 + y**2)**0.5
	if z <= 1:
		i2 = i2 + 1
	print(4*(i2 / i1))