#!/usr/bin/env python3

import argparse
import mcb185
import math

def entropy(a, c, g, t):
	e = 0
	length = a + c + g + t
	if length != 0:
		non_zero = []
		for n in [a, c, g, t]:
			if n != 0: non_zero.append(n)
		for n in non_zero:
			e -= n/length*math.log(n/length, 2)
		return e
		
parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, 
	default=20, help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, 
	default=1.4, help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help = 'soft mask')
arg = parser.parse_args()

window = []
indices = []
final_seq = []
for defline, seq in mcb185.read_fasta(arg.file):
	for s in seq: final_seq.append(s)
	for s in seq[0:arg.size]: window.append(s)
	a = 0
	c = 0
	g = 0
	t = 0
	for s in window:
		a += s.count('A')
		c += s.count('C')
		g += s.count('G')
		t += s.count('T')
	if arg.entropy >= entropy(a, c, g, t):
		indices.append(0) # create a list of indices of low complexity nt

	for i in range(1, len(seq) - arg.size + 1):
		window = window[1:]
		window.append(seq[i + arg.size - 1])
		a = 0
		c = 0
		g = 0
		t = 0
		for s in window:
			a += s.count('A')
			c += s.count('C')
			g += s.count('G')
			t += s.count('T')
		if arg.entropy >= entropy(a, c, g, t):
			indices.append(i)

	print(defline)
	for n in indices:
	
		#generate sequence with low-complexity regions marked as lower case
		if arg.lower:
			for i in range(arg.size + 1):
				if final_seq[n + i] == 'A': final_seq[n + i] = 'a'
				elif final_seq[n + i] == 'T': final_seq[n + i] = 't'
				elif final_seq[n + i] == 'C': final_seq[n + i] = 'c'
				elif final_seq[n + i] == 'G': final_seq[n + i] = 'g'
	print(defline)
	for i in range(0, len(seq), 60):
		sequence = ''.join(final_seq[i:i+60])
		print(sequence)
