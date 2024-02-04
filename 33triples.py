i = 0
for a in range(1, 100):
	for b in range(a, 100):
		c = (a**2 + b**2)**0.5
		if c.is_integer():
			i = i + 1
			print(i)
			print(a, b, int(c))