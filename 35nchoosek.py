def factorial(num):
	if num == 0 or num == 1:
		return 1
	else:
		return num * factorial(num - 1)

def nchoosek(n, k):
	if n < k:
		return 0
	else:
		return factorial(n) // (factorial(k) * factorial(n - k))


test = [(5, 2), (8, 3), (10, 5), (15, 7), (0, 1)]
for n, k in test:
	result = nchoosek(n, k)
	print(f"{n} choose {k} is {result}")