#!/usr/bin/env python3

from operator import itemgetter
import sys

current_neighbours=[]
curr=None
src=None
dest=None
# read the entire line from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	src, dest = line.split('\t')
	
	if (curr is None) or (curr==src):
		current_neighbours.append(dest)
		curr=src
	else:
		print('%s\t%s' % (curr , current_neighbours))
		curr=src
		current_neighbours=[]
		current_neighbours.append(dest)
	
# last src node

print('%s\t%s' % (curr,current_neighbours))

