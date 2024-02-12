import random

def saving_throw(DC, sit):
	n1 = random.randint(1, 20)
	if sit == 'norm':
		if n1 >= DC:
			return 1
		else: return 0
	elif sit == 'adv':
		n2 = random.randint(1, 20)
		if n1 >= n2: 
			if n1 >= DC: return 1
			else: return 0
		else:
			if n2 >= DC: return 1
			else : return 0
			
	elif sit == 'disadv':
		n2 = random.randint(1, 20)
		if n1 <= n2: 
			if n1 >= DC: return 1
			else: return 0
		else:
			if n2>= DC: return 1
			else : return 0		
		
def find_avg_probability(DC, sit):
	tot = 0
	for i in range(10000):
		result = saving_throw(DC, sit)
		tot = tot + result
	probability = tot/10000
	return probability