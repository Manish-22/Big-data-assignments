#!/usr/bin/env python3

import sys

statecity = {}

pres_state=""
pres_city=""
state_count=0
city_count=0
for line in sys.stdin:
    state, city = line.split(" ")
    state = state.strip()
    city = city.strip()

    if pres_state =="" or pres_state!=state:
        print(state,state_count)
        pres_state=state
        state_count=0
    state_count+=1
    if pres_city =="" or pres_city!=city:
        print(city,city_count)
        pres_city=city
        city_count=0
    city_count+=1

