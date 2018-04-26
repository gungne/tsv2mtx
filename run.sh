python tsv2mtx.py $1
cd output 
sort -k2,2n -k1,1nr temp.mtx >>matrix.mtx