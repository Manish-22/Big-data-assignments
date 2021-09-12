#!/usr/bin/env python3

import sys

hourcount= {}

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
