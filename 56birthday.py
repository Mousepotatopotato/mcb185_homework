import random
import sys

def find_same_birthdays(birthdays, people):
	for i in range(people):
		for j in range(i + 1, people):
			if birthdays[i] == birthdays[j]: 
				return 1
	return 0		
	
trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
hit = 0

for trial in range(trials):
	birthdays = []
	for i in range(people): birthdays.append(random.randint(1, days))
	hit += find_same_birthdays(birthdays, people)
	
print(f'probability: {hit/trials}')