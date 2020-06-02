from datetime import datetime
from calendar import day_name
startdate = datetime(2020, 2, 29, 0, 0, 0)
enddate = datetime.now()
print("Today is " + day_name[enddate.weekday()] + " " + str((enddate-startdate).days) + " March 2020")
