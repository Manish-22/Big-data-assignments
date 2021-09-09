#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import sys
import json
from datetime import datetime as dt


# reading entire line from STDIN (standard input)
for line in sys.stdin:
	# to remove leading and trailing whitespace
	line = line.strip()
	
	# read obj into dict
	data_dict = json.loads(line)
	
	# filter for map output
	if any(x in data_dict["Description"] for x in ["lane blocked", "shoulder blocked","overturned vehicle"]) :
		if data_dict["Severity"]>= 2:
			if data_dict["Sunrise_Sunset"]=="Night":
				if data_dict["Visibility(mi)"]<=10:
					if data_dict["Precipitation(in)"]>= 0.2:
						if any(x in data_dict["Weather_Condition"] for x in ["Heavy Snow", "Thunderstorm", "Heavy Rain", "Heavy Rain Showers" ,"Blowing Dust"]):
							time1=dt.strptime(data_dict["Start_Time"],"%Y-%m-%d %H:%M:%S")
							time2=dt.strptime(data_dict["End_Time"],"%Y-%m-%d %H:%M:%S")
							
							start_hour=int(time1.__str__()[-8:-6])
							end_hour=int(time2.__str__()[-8:-6])
							
							for i in range(start_hour,end_hour+1):
								print(i,1)
							
							
	

