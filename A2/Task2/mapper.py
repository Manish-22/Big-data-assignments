#!/usr/bin/env python3

import math
import json
import sys

src = None
dest = None

curr = None

v_path = sys.argv[1]
embedded_path = sys.argv[2]

f = open(embedded_path)
sim_matrix = []
data = json.load(f)
for i in range(len(data.items())):
	sim_matrix.append([0 for j in range(len(data.items()))])
for f1,f2 in data.items():
    temp = []
    s1 = [i*i for i in f2]   
    mag1 = math.sqrt(sum(s1))
    for f11,f22 in data.items():	
    	s2 = [i*i for i in f22]
    	mag2 = math.sqrt(sum(s2))
    	temp = [(f2[i] * f22[i]) for i in range(len(f2))]
    	w1 = sum(temp)/(mag1*mag2)
    	sim_matrix[int(f1)-1][int(f11)-1] = w1  



for line in sys.stdin:
    line = line.strip()
    src, neighbours = line.split('\t')
    #print("%s\t%s" % (src, neighbours))
    neighbours = neighbours.split(',')
    
    for ele in 
    




