#!/usr/bin/env python3

import sys
import json
import requests
from datetime import datetime as dt

r = requests.post("http://20.185.44.219:5000/",
                  data={"latitude": 40, "longitude": -66})

for line in sys.stdin:
    idk = line.strip()
    data_dic = json.loads(line)
    data_dic["Start_Lat"]
