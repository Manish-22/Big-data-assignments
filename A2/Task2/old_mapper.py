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
    prev_ranks[int(x)] = int(y)
f = open(embedded_path)
sim_matrix = []
data = json.load(f)
tra = [0 for i in range(len(data.items())+1)]
for i in range(len(data.items())):
    sim_matrix.append([0 for j in range(len(data.items()))])
for f1, f2 in data.items():
    temp = list()
    s1 = [i*i for i in f2]   # [1,2,3,4] ==> [1,4,8,16]
    mag1 = math.sqrt(sum(s1))
    for f11, f22 in data.items():
        # print(f1,f11)
        s2 = [i*i for i in f22]
        mag2 = math.sqrt(sum(s2))
        temp = [(f2[i] * f22[i]) for i in range(len(f2))]
        w1 = sum(temp)/(mag1*mag2)
        sim_matrix[int(f1)-1][int(f11)-1] = w1
# print(np.array(sim_matrix))


for line in sys.stdin:
    line = line.strip()
    src, neighbours = line.split('\t')
    tra[int(src)] = 1
    # print("%s\t%s" % (src, neighbours))
    neighbours = neighbours.replace(
        '[', '').replace(']', '').replace(' ', '').replace('\'', '').split(',')
    # print(neighbours)
    neighbours = [int(i) for i in neighbours]
    # print(neighbours)
    outgoing = len(neighbours)
    for i in range(1, len(data.items())+1):
        if i in neighbours:
            # print(i)
            # print(prev_ranks[int(src)])
            x = 1/outgoing
            sim_matrix[int(src)-1][i-1] = (prev_ranks[int(src)]
                                           * (sim_matrix[int(src)-1][i-1]))*x
        else:
            #print(src, i)
            sim_matrix[int(src)-1][i-1] = 0

for i in range(1, len(tra)):
    if not tra[i]:
        for j in range(len(data.items())):
            sim_matrix[i-1][j] = 0
# print(np.array(sim_matrix))
for i in range(len(data.items())):
    for j in range(len(data.items())):
        print(j+1, sim_matrix[i][j])


# read a line from stdin o(n) ==> for that node, obtain the vector from page embedding file o(1) ==> for every other vectors in page embedding file, compute the similarity o(n).
# Compute the contribution by using the given formula o(1)
