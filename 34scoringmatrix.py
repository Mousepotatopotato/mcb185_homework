def scoring_matrix(alphabet):
	print(f'  ', end='')
	for char1 in alphabet:
		print(f'{char1:>3}', end='')
	print()
	for char1 in alphabet:
		print(f'{char1} ', end=' ')
		for char2 in alphabet:
			score = '+1' if char1 == char2 else '-1'
			print(f'{score:>2}', end=' ')
		print()

scoring_matrix('ATCG')