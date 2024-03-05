import sys
import mcb185
import dogma
import itertools

k = 1
kcount = {}
missing_kmer = []
stop = False

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	rev_seq = dogma.revcomp(seq)
	while True:
		for s in [seq, rev_seq]:
			for i in range(len(s) - k + 1):
				kmer = s[i:i + k]
				if kmer not in kcount: kcount[kmer] = 0
				kcount[kmer] += 1
			
		for nts in itertools.product('ACGT', repeat=k):
			kmer = ''.join(nts)
			if kmer not in kcount:
				missing_kmer.append(kmer)
				stop = True
		k += 1
		if stop == True: 
			print(f'k = {k - 1}, {len(missing_kmer)}kmers: {missing_kmer}')
			break