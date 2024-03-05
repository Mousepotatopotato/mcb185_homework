d = {}
d = dict()
d = {'dog': 'woof', 'cat': 'meow'}
print(d)
d['pig'] = 'oink'
print(d)
import itertools
for nts in itertools.product('ACGT', repeat=2):
	print(nts)