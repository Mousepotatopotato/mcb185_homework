import gzip
import sys

def find_max(lengths):
	maximum = max(lengths)
	return maximum
	
def find_min(lengths):
	minumum = min(lengths)
	return minumum

def find_mean(lengths):
	total = 0
	for i in range(len(lengths)):
		total += lengths[i]
	mean = total/len(lengths)
	return mean
	
def find_sd(lengths, mean):
	sd_numerator = 0
	for i in range(len(lengths)): sd_numerator += ((lengths[i] - mean)**2)
	sd = (sd_numerator/len(lengths))**0.5
	return sd

def find_median(lengths):
	lengths.sort()
	middle = int(len(lengths)/2)
	if len(lengths) % 2 != 0: median = lengths[middle]
	elif len(lengths) % 2 == 0: median = (lengths[middle] + lengths[middle - 1])/2
	return median

	
gffpath = sys.argv[1]
feature = sys.argv[2]
lengths = []

with gzip.open(gffpath, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] != feature: continue
		lengths.append(int(words[4]) - int(words[3]) + 1)

print(f'count: {len(lengths)}')
print(f'min: {find_min(lengths)}')	
print(f'max: {find_max(lengths)}')
print(f'mean: {find_mean(lengths)}')
print(f'sd: {find_sd(lengths, find_mean(lengths))}')
print(f'median: {find_median(lengths)}')