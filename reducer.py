#!/usr/bin/env python

from operator import itemgetter
import sys

current_hour = None
current_count = 0
hour = None

# read the entire line from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# slpiting the data on the basis of tab we have provided in mapper.py
	hour, count = line.split('\t')
	# convert count (currently a string) to int
	try:
		count = int(count)
	except ValueError:
		# count was not a number, so silently
		# ignore/discard this line
		continue

	# this IF-switch only works because Hadoop sorts map output
	# by key (here: hour) before it is passed to the reducer
	if current_hour == hour:
		current_count += count
	else:
		if current_hour:
			# write result to STDOUT
			print('%s\t%s' % (current_hour, current_count))
		current_count = count
		current_hour = hour

# do not forget to output the last word if needed!
if current_hour == hour:
	print('%s\t%s' % (current_hour, current_count))
