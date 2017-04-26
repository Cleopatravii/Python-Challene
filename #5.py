import pickle
import sys

fin=open("banner.p","rb")
banner_out=pickle.load(fin)         

for line in banner_out:
     for char, count in line: sys.stdout.write(char*count)
     sys.stdout.write('\n')
