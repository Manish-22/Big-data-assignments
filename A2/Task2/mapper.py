#!/usr/bin/env python3

import math
import json
import sys
src = None
dest = None
curr = None

v_path = sys.argv[1]
embedded_path = sys.argv[2]
file1 = open(v_path, 'r')
Lines = file1.readlines()
prev_ranks = dict()
for line in Lines:
    x, y = line.strip().split(',')
    prev_ranks[int(x)] = float(y)


f = open(embedded_path)
embed_data = json.load(f)

tra = [0 for i in range(len(embed_data)+1)]

for line in sys.stdin:

    line = line.strip()
    src, neighbours = line.split('\t')
    neighbours = neighbours.replace(
        '[', '').replace(']', '').replace(' ', '').replace('\'', '').split(',')
    outgoing = len(neighbours)
    # print(neighbours)
    tra[int(src)] = 1
    contribution = [
        1/outgoing if str(i) in neighbours else 0 for i in range(1, len(embed_data)+1)]
    #print(src, embed_data)
    f22 = embed_data[src]
    s1 = [i*i for i in f22]
    mag1 = math.sqrt(sum(s1))
    for f1, f11 in embed_data.items():
        s2 = [i*i for i in f11]
        mag2 = math.sqrt(sum(s2))
        temp = [f11[i]*f22[i] for i in range(len(f11))]
        w1 = sum(temp)/(mag1*mag2)
        if int(f1) in prev_ranks:
        	contribution[int(f1)-1] *= w1*prev_ranks[int(f1)]
        else:
        	contribution[int(f1)-1] *=w1
        print(f1, contribution[int(f1)-1])
    #print(src, contribution)
# for i in range(1, len(tra)+1):
#     if not tra[i]:
#         print(i,)
