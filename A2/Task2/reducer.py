#!/usr/bin/env python3

import math
import json
import sys


curr = 0
contri = 0
for line in sys.stdin:
    x, y = line.split(' ')
    x = int(x)
    y = float(y)
    #print(x, y)
    if not curr:
        curr = int(x)
        contri += y
    elif curr != x:
        print(curr, '{0:.2f}'.format(0.15+0.85*contri), sep=',')
        curr = x
        contri = 0
    else:
        contri += y
print(curr, '{0:.2f}'.format(0.15+0.85*contri), sep=',')
