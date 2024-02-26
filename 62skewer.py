import dogma
import sys
import mcb185
# Sorry this homework is late, 
# but it took way loooooonger than I thought to debug

w = int(sys.argv[2])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	window = []
	for s in seq[0:w]: window.append(s)
	print(0, dogma.gc_comp(window), dogma.gc_skew(window))

	for i in range(1, len(seq) - w + 1):
		window = window[1:]
		window.append(seq[i + w - 1])
		print(i, dogma.gc_comp(window), dogma.gc_skew(window))

'''
	if w > 1:
		gc_comp += (-dogma.gc_comp(seq[i - 1]) + dogma.gc_comp(seq[i + w - 1]))/w
	else:
		gc_comp = dogma.gc_comp(seq[i])
	
	print(i, gc_comp)
	
# Will this be right way of doing it?
'''
	
	