import sys
import mcb185
import re
import json
import gzip

print(sys.argv[0][3])

d = [
    'hello',
    (3.14, 'pi'),
    [-1, 0, 1],
    {'year': 2000, 'month': 7}
]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])


truc = {
	'animals': {'dog': 'woof', 'cat': 'meow', 'pig': 'oink'},
	'numbers': [1.09, 2.72, 3.14],
	'is_complete': False,
}
print(json.dumps(truc, indent=4))


pwm_records = []
i = 0
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		i +=1
		print(line)
		if i >50: break