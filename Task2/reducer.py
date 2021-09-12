#!/usr/bin/env python3

import sys

statecity = {}

for line in sys.stdin:
    state, city = line.split(" ")
    state = state.strip()
    city = city.strip()

    if state not in statecity.keys():
        statecity[state] = 0
    statecity[state] += city

for state, city in statecity.items():
    print("{} {}".format(int(state), city))
