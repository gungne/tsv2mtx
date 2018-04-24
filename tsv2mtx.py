import os
import sys
import re
# import regex 
import numpy as np

tsv_file = open(sys.argv[1])
tsv_text = tsv_file.readlines()
ensembl_file = open('danrer10.txt')
ensemble_text = ensembl_file.readlines()

ensembl_records = dict()
for entry in ensemble_text[1:]:
	temp_entry = entry.split('\t')
	# print(temp_entry[2].upper())
	ensembl_records[re.sub('\n','',temp_entry[2].upper())] = temp_entry[0]

# print(ensembl_records)
if os.path.exists('output') ==False :
	os.mkdir('output')


## extract barcodes
barcodes = re.findall('[ATCG]*-1',tsv_text[0]);

barcodes_file = open('output/barcodes.tsv',"w+")
## output the barcode file
for item in barcodes:
	barcodes_file.write(item)
	barcodes_file.write('\n')


## processing the matrices
genes_file = open('output/genes.tsv',"w+")
matrices = tsv_text[1:]
missing_counter = 0
for record in matrices:
	#output the genes matrices
	keyword = re.sub('\"','',re.findall('\".*\"',record)[0])
	if keyword not in ensembl_records:
		ensembl_records[keyword] = 'ENDARGmissing' + str(missing_counter)
		missing_counter += 1 
	genes_file.write(ensembl_records[keyword])
	genes_file.write('\t')
	genes_file.write(keyword)
	genes_file.write('\n')