import sys
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
	''' simplified
	if a + c + g + t == 0:
		return 0
    
	elif a + c + g == 0:
		return -1*p_t*math.log(p_t, 2)
        
	elif a + c + t == 0:
		return -1*p_g*math.log(p_g, 2)
        
	elif a + t + g == 0:
		return -1*p_c*math.log(p_c, 2)

	elif c + t + g == 0:
		return -1*p_a*math.log(p_a, 2)
            
	elif a + c == 0:
		return -1*(p_t*math.log(p_t, 2) + p_g*math.log(p_g, 2))
    
	elif a + g == 0:
		return -1*(p_t*math.log(p_t, 2) + p_c*math.log(p_c, 2))
    
	elif a + t == 0:
		return -1*(p_c*math.log(p_c, 2) + p_g*math.log(p_g, 2))
    
	elif c + g == 0:
		return -1*(p_t*math.log(p_t, 2) + p_a*math.log(p_a, 2))
    
	elif c + t == 0:
		return -1*(p_a*math.log(p_a, 2) + p_g*math.log(p_g, 2))
    
	elif t + g == 0:
		return -1*(p_a*math.log(p_a, 2) + p_c*math.log(p_c, 2))
    
	elif a == 0:
		return -1*(p_t*math.log(p_t, 2) + 
		p_g*math.log(p_g, 2) + p_c*math.log(p_c, 2))
    
	elif c == 0:  
		return -1*(p_t*math.log(p_t, 2) + 
		p_g*math.log(p_g, 2) + p_a*math.log(p_a, 2))
    
	elif g == 0:
		return -1*(p_t*math.log(p_t, 2) + 
		p_a*math.log(p_a, 2) + p_c*math.log(p_c, 2))
    
	elif t == 0:
		return -1*(p_a*math.log(p_a, 2) + 
		p_g*math.log(p_g, 2) + p_c*math.log(p_c, 2))
    
	else:
		return -1* ((p_t * math.log(p_t, 2)) + (p_c * math.log(p_c, 2)) + 
		(p_g * math.log(p_g, 2)) + (p_a * math.log(p_a, 2)))
	'''
w = int(sys.argv[2])
limit_e = float(sys.argv[3])
window = []
indices = []
final_seq = []

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	for s in seq: final_seq.append(s)
	for s in seq[0:w]: window.append(s)
	a = 0
	c = 0
	g = 0
	t = 0
	for s in window:
		a += s.count('A')
		c += s.count('C')
		g += s.count('G')
		t += s.count('T')
	if limit_e >= entropy(a, c, g, t):
		indices.append(0) # create a list of indices of low complexity nt

	for i in range(1, len(seq) - w + 1):
		window = window[1:]
		window.append(seq[i + w - 1])
		a = 0
		c = 0
		g = 0
		t = 0
		for s in window:
			a += s.count('A')
			c += s.count('C')
			g += s.count('G')
			t += s.count('T')
		if limit_e >= entropy(a, c, g, t):
			indices.append(i)

	print(defline)
	for n in indices:
		#generate sequence with low-complexity regions marked as N
		for i in range(w + 1):
			final_seq[n + i] = 'N' 
	print(defline)
	for i in range(0, len(seq), 60):
		sequence = ''.join(final_seq[i:i+60])
		print(sequence)