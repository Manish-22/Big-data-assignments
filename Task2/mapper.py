#!/usr/bin/env python3

import sys
import json
import requests
from math import sqrt
from datetime import datetime as dt

if len(sys.argv) > 4:
    print("Too many args")
    sys.exit()

if len(sys.argv) < 4:
    print("need to give LA, LO ,D")
    sys.exit()

lat = float(sys.argv[1])
lng = float(sys.argv[2])
d = float(sys.argv[3])
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
url = "http://20.185.44.219:5000/"

for line in sys.stdin:
    idk = line.strip()
    data_dict = json.loads(line)
    startLat = float(data_dict["Start_Lat"])
    startLng = float(data_dict["Start_Lng"])
    dist = sqrt((startLat-lat)**2 + (startLng-lng)**2)
    if dist <= d:
        data = {"latitude": startLat, "longitude": startLng}
        r = requests.post(url, data=json.dumps(data), headers=headers).json()

        print(r["state"], r["city"],sep='\t')
