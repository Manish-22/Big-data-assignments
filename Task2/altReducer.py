#!/usr/bin/env python3

import sys

statecity = {}

pres_state = ""
pres_city = ""
state_count = 0
city_count = 0
flag = 1
for line in sys.stdin:
    state, city = line.split("\t")
    state = state.strip()
    city = city.strip()
    if flag:
        pres_state = state
        pres_city = city
        city_count = 1
        state_count += 1
        flag = 0
        print(pres_state)
    else:
        if pres_state != state:
            flag = 1
            print(pres_state, state_count)
            pres_state = state
            state_count = 1
            pres_city = city
            city_count = 1
        else:
            state_count += 1
            if pres_city != city:
                print(pres_city, city_count)
                pres_city = city
                city_count = 1
            else:
                city_count += 1
print(city, city_count)
print(state, state_count)
