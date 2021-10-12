#!/usr/bin/env python3

import sys

src=None
dest=None

curr=None

pages=[]
file = open("v.txt","w+")

for line in sys.stdin:
	line = line.strip()
	src,dest = line.split('\t')
	while(len(src)<7):
		src='0'+src
	print("%s\t%s" %(src,dest))
	
	if (curr is None) or curr!=src:
		pages.append(int(src))
		curr=src
		
#print(pages)
pages.sort()
#print(pages)
for i in pages:
	file.write(str(i)+',1\n')
