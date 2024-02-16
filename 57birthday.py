import random
import sys

def find_same_birthdays(calendar, people, days):
	for i in range(people):
		calendar[random.randint(0, days - 1)] += 1
	
	for num in calendar:
		if num >= 2: return 1
		
	return 0
	
trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])
hit = 0

for trial in range(trials):
	calendar = []
	for i in range(days): calendar.append(0)
	hit += find_same_birthdays(calendar, people, days)
	
print(f'probability: {hit/trials}')