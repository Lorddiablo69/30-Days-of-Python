# Introduction
# Pyhton Date time

import datetime
print(dir(datetime)) # with the help of dir function we can know the availaale functions

# getting datetime info

from datetime import datetime
now=datetime.now()
print(now)
day=now.day
month=now.month
year=now.year
hour=now.hour
minute=now.minute
second=now.second
timestamp=now.timestamp()
print(day,month,year,hour,minute)
print('timestamp',timestamp)
print(f'{day}/{month}/{year},{hour}:{minute}')

# formating date output using strftime
new_year=datetime(2025,1,1)
print(new_year)
day=new_year.day
month=new_year.month
year=new_year.year
hour=new_year.hour
minute=new_year.minute
second=new_year.second
print(day,month,year,hour,minute)
print(f'{day}/{month}/{year},{hour}:{minute}')

from datetime import datetime
now=datetime.now()
t=now.strftime('%H,%M:%S')
print('time:',t)
time_one=now.strftime('%m/%d/%Y,%H:%M:%S')
print('time one:',time_one)
time_two=now.strftime('%d/%m/%Y,%H:%M:%S')
print('time one:',time_two)

# string to time using strptime
from datetime import datetime
date_string = "18 November, 2025"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

# using date from datetime
from datetime import date
dd=date(2025,1,12)
print(dd)
print('current date:',dd.today())
today=date.today()
print('current year :',today.year)
print('current month :',today.month)
print('current day:',today.day)

# Time objects to represent time
from datetime import time
a=time()
print('a=',a)
b=time(10,30,50)
print('b=',b)
c=time(hour=10,minute=30,second=50)
print('c=',c)
d=time(10,30,50,200555)
print('d=',d)

# Difference between two points in time using
today = date(year=2019, month=12, day=5)
new_year = date(year=2025, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

t1 = datetime(year = 2019, month = 12, day = 5, hour = 0, minute = 59, second = 0)
t2 = datetime(year = 2025, month = 1, day = 1, hour = 0, minute = 0, second = 0)
diff = t2 - t1
print('Time left for new year:', diff) # Time left for new year: 26 days, 23: 01: 00

# Difference between tow points in time using timedelta
from datetime import timedelta
t1=timedelta(weeks=12,days=10,hours=4,seconds=20)
t2=timedelta(days=7,hours=5,minutes=3,seconds=30)
t3=t1-t2
print(t3)