import random

sequence = 10
for i in range(sequence):
	print()
	print(f'>seq-{i+1}')
	for i in range(random.randint(50, 60)):
		print(random.choice('ACGT',), end='')