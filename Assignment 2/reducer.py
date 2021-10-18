#!/usr/bin/env python3

from operator import itemgetter
import sys

current_neighbours=[]
curr=None
src=None
dest=None


file = open("v.txt","w+")

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
		current_neighbours=[]
		current_neighbours.append(dest)
		file.write(curr+',1\n')
		curr=src
		
# last src node

print('%s\t%s' % (curr,current_neighbours))
file.write(src+',1\n')


