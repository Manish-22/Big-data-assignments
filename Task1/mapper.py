#!/usr/bin/env python

import sys
import json
from datetime import datetime as dt
t = dict()

for line in sys.stdin:
    idk = line.strip()
    one_rec = json.loads(line)
    if(any(x in one_rec["Description"].lower() for x in ["lane blocked", "shoulder blocked", "overturned vehicle"]) and 
        type(one_rec["Description"]) != float and 
        type(one_rec["Weather_Condition"]) != float and
        one_rec["Severity"] >= 2 and one_rec["Sunrise_Sunset"] == "Night" and 
        one_rec["Visibility(mi)"] <= 10.0 and 
        one_rec["Precipitation(in)"] >= 0.2 and 
        any(y == one_rec["Weather_Condition"] for y in ["Heavy Snow", "Thunderstorm", "Heavy Rain", "Heavy Rain Showers", "Blowing Dust"])):
        time1 = one_rec["Start_Time"][11:13]
        print('%s\t%s' % (time1, 1))
