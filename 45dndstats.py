import random

n_stat = 6
def r3D6():
	for i in range(n_stat):
		stat = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
	return stat	
	
def r3D6r1():
	for i in range(n_stat):
		i1 = random.randint(1, 6)
		while i1 == 1:
			i1 = random.randint(1, 6)
			
		i2 = random.randint(1, 6)
		while i2 == 1:
			i2 = random.randint(1, 6)	
			
		i3 = random.randint(1, 6)
		while i3 == 1:
			i3 = random.randint(1, 6)			
		stat = i1 + i2 + i3
	return stat
	
def r3D6x2():
	for i in range(n_stat):
		i1 = random.randint(1, 6)
		i2 = random.randint(1, 6)
		if i1 <= i2: n1 = i2
		else: n1 = i1
		
		i1 = random.randint(1, 6)
		i2 = random.randint(1, 6)
		if i1 <= i2: n2 = i2
		else: n2 = i1
		
		i1 = random.randint(1, 6)
		i2 = random.randint(1, 6)
		if i1 <= i2: n3 = i2
		else: n3 = i1
		
		stat = n1 + n2 + n3
	return stat
	
def r4D6d1():
	for i in range(n_stat):
		i1 = random.randint(1, 6)
		i2 = random.randint(1, 6)
		i3 = random.randint(1, 6)
		i4 = random.randint(1, 6)
		if i1 <= i2:
			if i1 <= i3:
				if i1 <= i4:
					stat = i2 + i3 + i4
		
		if i2 <= i1:
			if i2 <= i3:
				if i2 <= i4:
					stat = i1 + i3 + i4
					
		if i3 <= i1:
			if i3 <= i2:
				if i3 <= i4:
					stat = i2 + i1 + i4
					
		if i4 <= i1:
			if i4 <= i2:
				if i4 <= i3:
					stat = i2 + i3 + i1		
	return stat
	
def find_avg(method):
	n1 = 0
	n2 = 0
	for i in range(10000):
		n2 = method()
		n1 = n1 + n2
	print(n1/10000)
	return
	
print('r3D6: ', end='')	
find_avg(r3D6)
print('r3D6r1: ', end='')	
find_avg(r3D6r1)
print('r3D6x2: ', end='')	
find_avg(r3D6x2)
print('r4D6d1: ', end='')	
find_avg(r4D6d1)
	