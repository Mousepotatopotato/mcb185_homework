#!/usr/bin/env python3

import argparse
import mcb185
import dogma

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', type=str, help='fasta file of mRNAs')
parser.add_argument('-m', '--min', type=int, 
	default=1, help='minimum protein length [%(default)i]')
parser.add_argument('-a', '--anti', action='store_true', 
	help = 'also examine the anti-parallel strand')
arg = parser.parse_args()


protein = []
num = 0

for defline, seq in mcb185.read_fasta(arg.file):
	#translate
	print(defline, seq)
	protein_seq = dogma.translate(seq)
	if arg.anti == True: 
		rev_seq = dogma.revcomp(seq)
		rev_protein_seq = dogma.translate(rev_seq)
	else: rev_protein_seq = ''
	
	for p_seq in [protein_seq, rev_protein_seq]:
		# start, end index initialize
		start_index = 'N'
		end_index = 'N'
		for i in range(len(p_seq)):
			if p_seq[i] == 'M':
				if start_index == 'N':
					start_index = i
			elif p_seq[i] == '*':
				if start_index != 'N' and end_index == 'N':
					end_index = i
					if end_index - start_index >= arg.min:
						protein.append(p_seq[start_index:end_index])
						print(f'>{defline}')
						for i in range(0, len(protein[num]), 60):
							sequence = ''.join(protein[num][i:i+60])
							print(sequence)
						num += 1
					#start_index = 'N'
					#end_index = 'N'
		start_index = 'N'

