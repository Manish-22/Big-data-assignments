#!/usr/bin/env python3

from operator import itemgetter
import sys

current_hour = None
current_count = 0
hour = None

# read the entire line from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	hour, count = line.split('\t',1)
	try:
		count = int(count)
	except ValueError:
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: hour) before it is passed to the reducer
	if current_hour == hour:
		current_count += count
	else:
		if current_hour:
			if current_hour[0]=='0':
				print('%s\t%s' % (current_hour[1:], current_count))
			else:
				print('%s\t%s' % (current_hour, current_count))
		current_count = count
		current_hour = hour

# do not forget to output the last word if needed!
if current_hour[0]=='0':
	print('%s\t%s' % (current_hour[1:], current_count))
else:
	print('%s\t%s' % (current_hour, current_count))
