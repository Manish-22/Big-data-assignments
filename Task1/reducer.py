#!/usr/bin/env python3

import sys

'''hourcount= {}

for line in sys.stdin:
    hour, count = line.split("\t")
    hour = hour.strip()
    count = count.strip()

    try:
        count = int(count)
    except ValueError:
        continue

    if hour not in hourcount.keys():
        hourcount[hour] = 0
    hourcount[hour]+= count

for hour, count in hourcount.items():
    print("{} {}".format(int(hour), count))
'''
for line in sys.stdin:
     line = line.strip()
     hour, count = line.split('\t')
     try:
         count = int(count)
     except ValueError:
         continue

     if current_hour == hour:
         current_count += count
     else:
         if current_hour:
             print(int(current_hour), " ", current_count, sep="")
         current_count = count
         current_hour = hour

# # do not forget to output the last hour if needed!
 if current_hour == hour:
     print(int(current_hour), " ", current_count, sep="")
