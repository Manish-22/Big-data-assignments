#!/usr/bin/env python3

import math
import json
import sys

src = None
dest = None

curr = None


for line in sys.stdin:
    line = line.strip()
    src, dest = line.split('\t')
    print("%s\t%s" % (src, dest))

#!/usr/bin/env python3


src = None
dest = None

curr = None


# for line in sys.stdin:
# 	line = line.strip()
# 	src,dest = line.split('\t')
# 	print("%s\t%s" %(src,dest))
f = open('embedding-sample.json')
sim_matrix = list()
data = json.load(f)
for i in range(len(data.items())):
    sim_matrix.append([0 for j in range(len(data.items()))])
for f1, f2 in data.items():
    temp = list()
    s1 = [i*i for i in f2]   # [1,2,3,4] ==> [1,4,8,16]
    mag1 = math.sqrt(sum(s1))
    for f11, f22 in data.items():
        print(f1, f11)
        s2 = [i*i for i in f22]
        mag2 = math.sqrt(sum(s2))
        temp = [(f2[i] * f22[i]) for i in range(len(f2))]
        w1 = sum(temp)/(mag1*mag2)
        sim_matrix[int(f1)-1][int(f11)-1] = w1
print(sim_matrix)
