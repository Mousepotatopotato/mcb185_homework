import sys

def dtc(P, Q):
    d = 0
    for p, q in zip(P, Q):
        d += abs(p - q)
    return d #Oh, busted! Caught red-handed, I see. I must say, I applaud...

colorfile = sys.argv[1]
input_RGB = [int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])]
#This crap has been moved to line16
distance = 99999

with open(colorfile) as fp:
	for line in fp:
		file_RGB = [0, 0, 0]
		words = line.split()
		elements = words[2].split(',')
		for i in range(3):
				file_RGB[i] = int(elements[i])
		new_dis = dtc(input_RGB, file_RGB)
		if new_dis < distance: 
			distance = new_dis
			color = words[0]

print(f'Color: {color}')
