import random

# don't use global variable 
def r3D6():
	stat = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
	return stat	
	
def r3D6r1():
	stat = 0
	for i in range(3):
		dice = random.randint(1, 6)
		if dice == 1:
			dice = random.randint(1, 6)			
			stat += dice
		else: stat += dice

	return stat
	
def r3D6x2():
	stat = 0
	for i in range(3):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 <= d2: stat += d2
		else: stat += d1
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
