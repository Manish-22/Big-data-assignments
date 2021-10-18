#!/usr/bin/env python3

import sys

src=None
dest=None

curr=None


for line in sys.stdin:
	line = line.strip()
	src,dest = line.split('\t')
	print("%s\t%s" %(src,dest))
    
    