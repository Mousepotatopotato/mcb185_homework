import gzip
lengths = []
path = '../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz'
i = 0

with gzip.open(path, 'rt') as fp:
	for line in fp:
		if line[0] == '#': continue
		words = line.split()
		if words[2] != 'CDS': continue
		lengths.append(int(words[4]) - int(words[3]) + 1) #begin - end coordinates
		print(lengths[i])
		i += 1