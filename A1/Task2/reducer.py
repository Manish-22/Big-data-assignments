#!/usr/bin/env python3

import sys

statecity = {}

pres_state = ""
pres_city = ""
state_count = 0
city_count = 0

for line in sys.stdin:
    line = line.strip()
    state, city = line.split("\t")
    state = state[0:2]

    if pres_state == "":
        pres_state = state
        pres_city = city
        state_count = 0
        city_count = 1
        print(pres_state)

    elif pres_state != state:
        print(pres_city, city_count)
        state_count += city_count
        print(pres_state, state_count)
        pres_city = city
        pres_state = state
        state_count = 0
        city_count = 1
        print(pres_state)

    elif pres_city != city:
        print(pres_city, city_count)
        state_count += city_count
        pres_city = city
        city_count = 1
    else:
        city_count += 1


print(pres_city, city_count)
print(pres_state, state_count+city_count)
