import sys
import mcb185
import re
import json
import gzip

def revcomp(dna):
	rc = []
	for nt in dna[::-1]:
		if   nt == 'a': rc.append('t')
		elif nt == 'c': rc.append('g')
		elif nt == 'g': rc.append('c')
		elif nt == 't': rc.append('a')
		else: rc.append('N')
	return ''.join(rc)
	
sequence = ''
sequences = []
joined_seq = ''
position = []

for i in range(14):
	nt_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
	position.append(nt_count)
	
# extract the sequence
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if re.search('ORIGIN', line): 
			break
	for line in fp:
		if line.startswith('//'):
			joined_seq = ''.join(sequences)
		else:	
			sequence = ''.join(line.rstrip().split()[1:])
			sequences.append(sequence)
		
#find PWM
with gzip.open(sys.argv[1], 'rt') as fp:		
	for line in fp:
		start_i = ''
		end_i = ''
		#extract the start and end index from file
		if line.startswith('     CDS'):
			seq = ''
			index = line.rstrip().split()[1]
			if re.search('complement\(join|join', line):
				pass #do nothing, only to exclude the conditions
			elif re.search('complement', line): 
				end_i = index.split('..')[-1]
				end_i = end_i.split(')')[0]
				seq = revcomp(joined_seq[int(end_i)-5:int(end_i)+9])
			else: 
				start_i = index.split('..')[0]
				seq = joined_seq[int(start_i)-10:int(start_i)+4]
			#input data	
			position_i = 0
			for nt in seq:
				if nt == 'a': position[position_i]['A'] += 1
				elif nt == 'c': position[position_i]['C'] += 1
				elif nt == 'g': position[position_i]['G'] += 1
				elif nt == 't': position[position_i]['T'] += 1
				position_i += 1
	#print table			
	print('AC IMTSU001')
	print('XX')
	print('ID ECKOZ')
	print('DE I made this shit up')
	print('PO      A       C       G       T')
	for i in range(14):
		A = 'A'
		C = 'C'
		G = 'G'
		T = 'T'
		print(f'{i+1:<8}{position[i][A]:<8}{position[i][C]:<8}
		{position[i][G]:<8}{position[i][T]:<8}')
	print('XX')