#!/usr/bin/env python

# import sys because we need to read and write data to STDIN and STDOUT
import sys
import json


count=0
# reading entire line from STDIN (standard input)
for line in sys.stdin:
	# to remove leading and trailing whitespace
	line = line.strip()
	
	# read obj into dict
	data_dict = json.loads(line)
	
	# filter for map output
	if "lane blocked" in data_dict["Description"] or "shoulder blocked" in data_dict["Description"] or data_dict["Description"]=="overturned vehicle":
		if data_dict["Severity"]>= 2:
			if data_dict["Sunrise_Sunset"]=="Night":
				if data_dict["Visibility(mi)"]<=10:
					if data_dict["Precipitation(in)"]>= 0.2:
						if data_dict["Weather_Condition"]=="Heavy Snow" or data_dict["Weather_Condition"]=="Thunderstorm" or data_dict["Weather_Condition"]=="Heavy Rain Showers" or data_dict["Weather_Condition"]=="Blowing Dust":
							print(data_dict) 
	
print(f"{count} no. of obj")
