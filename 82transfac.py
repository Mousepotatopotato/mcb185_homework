import sys
import mcb185
import re
import json
import gzip

pwm_records = []

with gzip.open(sys.argv[1], 'rt') as fp:
	record = {}
	pwm = []
	
	for line in fp:
		# identify and store ID
		if line.startswith('ID'):
			# store into pwm_records and clean
			if record:
				record['pwm'] = pwm
				pwm_records.append(record)
				record = {}
				pwm = []
			record['id'] = line.rstrip().split(' ')[1]
		# identify and store PWM values. I looked online about regular expressions
		if re.search('^\d{2}', line): pwm.append({'A': line.rstrip().split()[1],
			'C': line.rstrip().split()[2], 'G': line.rstrip().split()[3], 
			'T': line.rstrip().split()[4]})
	# for the last record
	if record:
		record['pwm'] = pwm
		pwm_records.append(record)
	print(json.dumps(pwm_records, indent=4))

	