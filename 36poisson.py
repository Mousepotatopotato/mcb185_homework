import math
def poisson(n, k):
	return (n**k * math.e**(-n)) / math.factorial(k)
	
test = [(2, 1), (10, 9), (8, 8)]
for n, k in test:
	result = poisson(n, k)
	print(f'Poisson probability for n={n} and k={k}: {result}')