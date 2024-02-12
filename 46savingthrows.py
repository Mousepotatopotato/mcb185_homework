import random

def saving_throw(DC, sit):
	n1 = random.randint(1, 20)
	if sit == 0:
		if n1 >= DC:
			return 1
		else: return 0
	elif sit == 1:
		n2 = random.randint(1, 20)
		if n1 >= n2: 
			if n1 >= DC: return 1
			else: return 0
		else:
			if n2 >= DC: return 1
			else : return 0
			
	elif sit == 2:
		n2 = random.randint(1, 20)
		if n1 <= n2: 
			if n1 >= DC: return 1
			else: return 0
		else:
			if n2>= DC: return 1
			else : return 0		
		
def find_avg(DC, sit):
	tot = 0
	for i in range(10000):
		n1 = saving_throw(DC, sit)
		tot = tot + n1
	print(tot/10000, end='  ')
	
print('DC norm     adv     dis')
print(5, end='  ')
find_avg(5, 0)
find_avg(5, 1)
find_avg(5, 2)
print()
print(10, end=' ')
find_avg(10, 0)
find_avg(10, 1)
find_avg(10, 2)
print()
print(15, end=' ')
find_avg(15, 0)
find_avg(15, 1)
find_avg(15, 2)