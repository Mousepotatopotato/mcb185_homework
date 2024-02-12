import random

total = 0
hit = 0
while True:
	total = total + 1
	x = random.random()
	y = random.random()
	distance = (x**2 + y**2)**0.5
	if distance <= 1:
		hit = hit + 1
	print(4*(hit / total))