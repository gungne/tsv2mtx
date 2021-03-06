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
if os.path.exists('output') == False :
	os.mkdir('output')


## extract barcodes
barcodes = re.findall('[ATCG]*-1',tsv_text[0]);

barcodes_file = open('output/barcodes.tsv',"w+")
## output the barcode file
for item in barcodes:
	barcodes_file.write(item)
	barcodes_file.write('\n')

cell_number = len(barcodes)
# print(cell_number)

## processing the matrices
genes_file = open('output/genes.tsv',"w+")
temp_file = open('output/temp.mtx',"w+")
matrix_file = open('output/matrix.mtx',"w+")
matrix_file.write('%%MatrixMarket matrix coordinate integer general\n')
matrix_file.write('%\n')

matrices = tsv_text[1:]
# print(len(matrices))
# matrix_file.write(str(len(matrices))+' '+str(len(barcodes))+' '+str(len(matrices)*len(barcodes))+'\n')

missing_counter = 0
row_count = 0 
item_count = 0
for record in matrices:
	#output the genes matrices
	record = re.sub('\n','',record)
	keyword = re.sub('\"','',re.findall('\".*\"',record)[0])
	keyword = re.sub('\(.*\)','',keyword)
	if keyword not in ensembl_records:
		ensembl_records[keyword] = 'ENDARGmissing' + str(missing_counter)
		missing_counter += 1 
		continue
	genes_file.write(ensembl_records[keyword])
	genes_file.write('\t')
	genes_file.write(keyword)
	genes_file.write('\n')

	# output the matrice to mtx
	
	values = record.split(' ')[1:]
	column_count = 0
	for num_value in values:
		if str(num_value) != '0':
			temp_file.write(str(row_count+1)+' '+str(column_count+1)+' '+str(num_value))
			temp_file.write('\n')
			item_count += 1
		column_count += 1 

	row_count += 1
			# print(column_count)


matrix_file.write(str(row_count)+' '+str(len(barcodes))+' '+str(item_count)+'\n')
			

	# print(column_count)
