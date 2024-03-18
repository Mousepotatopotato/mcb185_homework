#!/usr/bin/env python3

import argparse
import mcb185
import gzip
#efficient way using dict
parser = argparse.ArgumentParser(prog='variants', 
	description='variant reporter')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()

chrom_dict = {}
var_region = {}
region = 0
i = 0

gff = {}

with gzip.open(arg.gff, 'rt') as fp:
	for line in fp:
		start_i = 0
		end_i = 0
		chrom = line.rstrip().split()[0]
		category = line.rstrip().split()[2]
		start_i = int(line.rstrip().split()[3])
		end_i = int(line.rstrip().split()[4])
		indices = [start_i, end_i, category]
		if chrom not in gff:
			gff[chrom] = []
		gff[chrom].append(indices)
results = []
with gzip.open(arg.vcf, 'rt') as fp:
	for line in fp:
		chrom = line.rstrip().split()[0]
		position = int(line.rstrip().split()[1])
		categories = []
		for start, end, cat in gff[chrom]:
			if position >= start and position <= end:
				if cat not in categories:
					categories.append(cat)
		result = {'chrom': chrom, 'position': position, 
			'categories': ', '.join(categories)}
		if categories: results.append(result)
for result in results:
	chrom = 'chrom'
	position = 'position'
	categories = 'categories'
	print(f'{result[chrom]:<8}{result[position]:<8}{result[categories]:<8}')			
			
'''
		for gff_dict in gff_list:
			if position >= gff_dict['start'] and position <= gff_dict['end']:
				if chrom == gff_dict['chrom']:
					if gff_dict['category'] not in categories:
						categories.append(gff_dict['category'])
		result = {'chrom': chrom, 'position': position, 
			'categories': ', '.join(categories)}
		if categories: results.append(result)

for result in results:
	chrom = 'chrom'
	position = 'position'
	categories = 'categories'
	print(f'{result[chrom]:<8}{result[position]:<8}{result[categories]:<8}')
'''