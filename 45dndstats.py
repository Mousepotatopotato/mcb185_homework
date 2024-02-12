import random

# don't use global variable 
def r3D6():
	stat = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
	return stat	
	
def r3D6r1():

	d1 = random.randint(1, 6)
	while d1 == 1:
		d1 = random.randint(1, 6)			
		
	d2 = random.randint(1, 6)
	while d2 == 1:
		d2 = random.randint(1, 6)	
			
	d3 = random.randint(1, 6)
	while d3 == 1:
		d3 = random.randint(1, 6)			
	stat = d1 + d2 + d3
	return stat
	
def r3D6x2():
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	if d1 <= d2: n1 = d2
	else: n1 = d1
		
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	if d1 <= d2: n2 = d2
	else: n2 = d1
		
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	if d1 <= d2: n3 = d2
	else: n3 = d1
		
	stat = n1 + n2 + n3
	return stat
	
def r4D6d1():
	d1 = random.randint(1, 6)
	d2 = random.randint(1, 6)
	d3 = random.randint(1, 6)
	d4 = random.randint(1, 6)
	if d1 <= d2 and d1 <= d3 and d1 <= d4:
		stat = d2 + d3 + d4	
		
	if d2 <= d1 and d2 <= d3 and d2 <= d4:
		stat = d1 + d3 + d4
					
	if d3 <= d1 and d3 <= d2 and d3 <= d4:
		stat = d2 + d1 + d4
					
	if d4 <= d1 and d4 <= d2 and d4 <= d3:
		stat = d2 + d3 + d1		
	return stat
	
def find_avg_stat(method):
	tot_stat = 0
	stat = 0
	for i in range(10000):
		stat = method()
		tot_stat += stat
	avg_stat = tot_stat/10000
	return avg_stat
	
print('r3D6: ', find_avg_stat(r3D6))	
print('r3D6x2: ', find_avg_stat(r3D6x2))	
print('r3D6r1: ', find_avg_stat(r3D6r1))	
print('r4D6d1: ', find_avg_stat(r4D6d1))	
