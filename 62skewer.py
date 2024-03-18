import dogma
import sys
import mcb185
# Sorry this homework is late, 
# but it took way loooooonger than I thought to debug

w = int(sys.argv[2])
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	window = seq[0:w]
	g_count = window.count('G')
	c_count = window.count('C')
	gc_comp = (g_count + c_count) / w
	gc_skew = (g_count - c_count) / (g_count + c_count)
	print(0, gc_comp, gc_skew)
	drop = window[0]
	for i in range(1, len(seq) - w):
		gain = seq[i + w]
		if gain == 'C':
			c_count += 1
		elif gain == 'G':
			g_count += 1
		if drop == 'C':
			c_count -= 1
		elif drop == 'G':
			g_count -= 1
			
		gc_comp = (g_count + c_count) / w
		gc_skew = (g_count - c_count) / (g_count + c_count)	
		print(i, gc_comp, gc_skew)

'''
	if w > 1:
		gc_comp += (-dogma.gc_comp(seq[i - 1]) + dogma.gc_comp(seq[i + w - 1]))/w
	else:
		gc_comp = dogma.gc_comp(seq[i])
	
	print(i, gc_comp)
	
# Will this be right way of doing it?
'''
	
	