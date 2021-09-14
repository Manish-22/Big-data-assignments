#!/usr/bin/env python3

import sys

statecity = {}

pres_state = ""
pres_city = ""
state_count = 0
city_count = 0

city = ""
state= ""
pres_city=""
pres_state=""
for line in sys.stdin:
    state, city = line.split("\t")
    state = state.strip()
    city = city.strip()

    if pres_state == "":
        print(state)
        pres_state = state
        state_count = 0
    if pres_city == "":
        pres_city = city
    if pres_city != city:
        if " " in pres_city:
            print(pres_city, city_count)
        else:
            print(pres_city[:-1],city_count)
        pres_city = city
        city_count = 0
    city_count += 1
    if pres_state != state:
        print(pres_state, state_count)
        print(state)
        pres_state = state
        state_count = 0
    state_count += 1
# Last record
if(" " in pres_city):
    print(pres_city, city_count)
else:
    print(pres_city[:-1],city_count)
print(state, state_count)
