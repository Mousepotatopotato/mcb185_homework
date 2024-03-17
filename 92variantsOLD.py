#!/usr/bin/env python3

import argparse
import mcb185
import gzip

parser = argparse.ArgumentParser(description='variant reporter.')
parser.add_argument('gff', type=str, help='GFF file')
parser.add_argument('vcf', type=str, help='VCF file')
arg = parser.parse_args()

#extract and store all variant region
chrom_dict = {}
var_region = {}
old_region = 0
new_region = 0
duplicate_region = []
with gzip.open(arg.vcf, 'rt') as fp:
	for line in fp:
		new_region = int(line.rstrip().split()[1])
		#Write the regions into dict
		if new_region > old_region:
			old_region = new_region
			var_region[new_region] = ''
		elif old_region == new_region:
			old_region = new_region
			duplicate_region.append(new_region)
		elif new_region < old_region:
			old_region = new_region
			chrom_dict[chrom] = var_region
			var_region = {}
			var_region[new_region] = ''
		chrom = line.rstrip().split()[0]		
chrom_dict[chrom] = var_region #append the last one

#find genes that match the region
with gzip.open(arg.gff, 'rt') as fp:
	for line in fp:
		chrom = line.rstrip().split()[0]
		start_i = 0
		end_i = 0
		category = line.rstrip().split()[2]
		start_i = int(line.rstrip().split()[3])
		end_i = int(line.rstrip().split()[4])
		
		# store the catagories
		if chrom in chrom_dict:
			for var in chrom_dict[chrom]:
				if var >= start_i and var <= end_i:
					chrom_dict[chrom][var] += f'{category}, '
					
	#remove duplicate categories
	for chrom, var_reg in chrom_dict.items():
		for region, cat in var_reg.items():
			cats = cat.split(', ')	
			unique_category = []
			for cat in cats:
				if cat not in unique_category:
					if cat != '':
						unique_category.append(cat)	
			chrom_dict[chrom][region] = ', '.join(unique_category)
			
			#print output
			if chrom_dict[chrom][region] != '':
				print(f'{chrom:<8}{region:<8}{chrom_dict[chrom][region]:<8}')