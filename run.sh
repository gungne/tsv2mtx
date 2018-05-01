python tsv2mtx.py $1

sort -k2,2n -k1,1nr output/temp.mtx >>output/matrix.mtx

rm output/temp.mtx