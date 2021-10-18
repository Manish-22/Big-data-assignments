#!/usr/bin/env python3

import sys

for line in sys.stdin:
	line = line.strip()
	src,dest = line.split('\t')
	print("%s\t%s" %(src,dest))
	
	
