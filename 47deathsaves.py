import random

def death_saves():
	fail = 0
	success = 0
	conidtion = 0
	while True:	
		n1 = random.randint(1, 20)
		if n1 < 10: 
			if n1 == 1:
				fail += 2
			else: fail += 1
		elif n1 >= 10: 
			success += 1
			if n1 == 20: 
					condition = 2
					break 
					
		if fail >= 3:
			condition = 0
			break
			
		if success >= 3:
			condition = 1
			break
			
	return condition 


stabilize = 0
die = 0
revive = 0	
for i in range(10000):
	condition = death_saves()
	if condition == 0:
		die += 1
	if condition == 1:
		stabilize += 1
	if condition == 2:
		revive += 1

print(f'die: {die/10000}')
print(f'stabilize: {stabilize/10000}')
print(f'revive: {revive/10000}')