import sys
import mcb185
import dogma

orf_l = int(sys.argv[2])
protein = []
num = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	rev_seq = dogma.revcomp(seq)

	for frame in range(3):
		protein_seq = dogma.translate(seq[frame:])
		rev_protein_seq = dogma.translate(rev_seq[frame:])
		
		start_index = 'N' # initialize start index
		for p_seq in [protein_seq, rev_protein_seq]:
			for i in range(len(p_seq)):
				if p_seq[i] == 'M':
					if start_index == 'N':
						start_index = i
				elif p_seq[i] == '*':
					if start_index != 'N':
						end_index = i
						if end_index - start_index >= orf_l:
							protein.append(p_seq[start_index:end_index])
							print(f'{num}	{defline[:11]}	CDS	{start_index}	{end_index}')
							num += 1
						start_index = 'N'		
			start_index = 'N'