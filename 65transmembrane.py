import sys
import mcb185
import dogma

def calc_KD(seq):
	KD = 0
	for aa in seq:
		if(aa == 'A'):
			KD += 1.8
		elif(aa == 'C'):
			KD +=  2.5
		elif(aa == 'D'):
			KD +=  -3.5
		elif(aa == 'E'):
			KD +=  -3.5
		elif(aa == 'F'):
			KD +=  2.8					
		elif(aa == 'G'):
			KD +=  -0.4					
		elif(aa == 'H'):
			KD +=  -3.2				
		elif(aa == 'I'):
			KD +=  4.5					
		elif(aa == 'K'):
			KD +=  -3.9					
		elif(aa == 'L'):
			KD +=  3.8					
		elif(aa == 'M'):
			KD +=  1.9				
		elif(aa == 'N'):
			KD +=  -3.5				
		elif(aa == 'P'):
			KD +=  -1.6					
		elif(aa == 'Q'):
			KD +=  -3.5				
		elif(aa == 'R'):
			KD +=  -4.5					
		elif(aa == 'S'):
			KD +=  -0.8					
		elif(aa == 'T'):
			KD +=  -0.7		
		elif(aa == 'V'):
			KD +=  4.2			
		elif(aa == 'W'):
			KD +=  -0.9			
		elif(aa == 'Y'):
			KD +=  -1.3
			
	avg_KD = KD/len(seq)
	return avg_KD

w_sp = 8
w_transm = 11
num = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	hphobic_sp = False
	# if I don't need part of the redundancy, should I still make it a function?
	for i in range(31 - w_sp):
		if len(seq[i:i + w_sp]) == w_sp:
			if calc_KD(seq[i:i + w_sp]) >= 2.5:
				if seq[i:i + w_sp].count('P') == 0:
					hphobic_sp = True
					break
					
	if hphobic_sp: 
		for i in range(29, len(seq) - w_transm):
			if calc_KD(seq[i:i + w_transm]) >= 2:
				if seq[i:i + w_transm].count('P') == 0:
					print(num, defline[:50])
					num += 1
					break
						
				