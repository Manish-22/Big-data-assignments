import sys 
import json
from datetime import datetime as dt
count=0
for line in sys.stdin:
    line =line.strip()
    
    data_dict = json.loads(line)

    if(any(x in data_dict["Description"] for x in ["lane blocked", "shoulder blocked","overturned vehicle"]) and data_dict["Severity"]>=2 and data_dict["Sunrise_Sunset"]=="Night" and data_dict["Visibility(mi)"]<=10 and data_dict["Precipitation(in)"]>= 0.2 and any(y in data_dict["Weather_Condition"] for y in ["Heavy Snow", "Thunderstorm", "Heavy Rain", "Heavy Rain Showers" ,"Blowing Dust"])):
        time1=dt.strptime(data_dict["Start_Time"],"%Y-%m-%d %H:%M:%S")
        time2=dt.strptime(data_dict["End_Time"],"%Y-%m-%d %H:%M:%S")
							
        start_hour=int(time1.__str__()[-8:-6])
        end_hour=int(time2.__str__()[-8:-6])

        if(end_hour-start_hour>1):
            print("start Hour",start_hour)
        #print(data_dict["Weather_Condition"])
        print(start_hour)
        #print("count",count)
        count+=1