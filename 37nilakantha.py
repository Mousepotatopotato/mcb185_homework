def estimate_pi(repeats):
	pi = 3.0
	sign = 1
	
	for i in range(1, repeats + 1):
		pi = pi + sign * (4/(2*i * (2*i + 1) * (2*i + 2)))
		sign = -1 * sign
	return pi
	
repeats = 100
pi = estimate_pi(repeats)
print(f'Estimated value of pi with {repeats} repeats: {pi}')

repeats = 200
pi = estimate_pi(repeats)
print(f'Estimated value of pi with {repeats} repeats: {pi}')