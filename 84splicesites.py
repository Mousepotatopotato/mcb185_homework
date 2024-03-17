import sys
import mcb185
import re
import json
import gzip

def input_position_data(position, seq):
	position_i = 0
	for nt in seq:
		if nt == 'A': position[position_i]['A'] += 1
		elif nt == 'C': position[position_i]['C'] += 1
		elif nt == 'G': position[position_i]['G'] += 1
		elif nt == 'T': position[position_i]['T'] += 1
		position_i += 1
	return position

sequence = []
acceptor_position = []
donor_position = []

for i in range(7):
	nt_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
	acceptor_position.append(nt_count)
for i in range(6):
	nt_count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
	donor_position.append(nt_count)

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	sequence.append(seq)

with gzip.open(sys.argv[2], 'rt') as fp:
	i = 0
	for line in fp:
		if re.search('RNASeq_splice', line):
			acceptor_seq = ''
			donor_seq = ''
			index = line.rstrip().split()[3:5]
			# I didn't come up with a way to put this into a loop. 
			#It tells me that startswith can only take 3 arguments at most 
			if line.startswith('I	'):
				acceptor_seq = sequence[0][int(index[1]) - 7:int(index[1])]
				donor_seq = sequence[0][int(index[0]) - 1:int(index[0]) + 5]
			elif line.startswith('II	'):
				acceptor_seq = sequence[1][int(index[1]) - 7:int(index[1])]
				donor_seq = sequence[1][int(index[0]) - 1:int(index[0]) + 5]
			elif line.startswith('III	'):
				acceptor_seq = sequence[2][int(index[1]) - 7:int(index[1])]
				donor_seq = sequence[2][int(index[0]) - 1:int(index[0]) + 5]
			elif line.startswith('IV	'):
				acceptor_seq = sequence[3][int(index[1]) - 7:int(index[1])]
				donor_seq = sequence[3][int(index[0]) - 1:int(index[0]) + 5]
			elif line.startswith('V	'):
				acceptor_seq = sequence[4][int(index[1]) - 7:int(index[1])]
				donor_seq = sequence[4][int(index[0]) - 1:int(index[0]) + 5]
			elif line.startswith('X	'):
				acceptor_seq = sequence[5][int(index[1]) - 7:int(index[1])]
				donor_seq = sequence[5][int(index[0]) - 1:int(index[0]) + 5]
				
			input_position_data(acceptor_position, acceptor_seq)
			input_position_data(donor_position, donor_seq)
	
	#print table			
	print('AC DEMO1')
	print('XX')
	print('ID ACC')
	print('DE splice acceptor')
	print('PO      A       C       G       T')
	for i in range(7):
		A = 'A'
		C = 'C'
		G = 'G'
		T = 'T'
		print(f'{i+1:<8}{acceptor_position[i][A]:<8}{acceptor_position[i][C]:<8}
		{acceptor_position[i][G]:<8}{acceptor_position[i][T]:<8}')
	print('XX')
	print('//')
	print('AC DEMO2')
	print('XX')
	print('ID DON')
	print('DE splice donor')
	print('PO      A       C       G       T')
	for i in range(6):
		A = 'A'
		C = 'C'
		G = 'G'
		T = 'T'
		print(f'{i+1:<8}{donor_position[i][A]:<8}{donor_position[i][C]:<8}
		{donor_position[i][G]:<8}{donor_position[i][T]:<8}')
	print('XX')
	print('//')
	
